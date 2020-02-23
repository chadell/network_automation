import os
import json
import napalm
import jinja2
import pprint


PATCH_FILENAME = os.path.expanduser("~/config_patch")

with open("assignement_1.json") as input_data:
    network_data = json.load(input_data)

driver = napalm.get_network_driver('vyos')

device_config = {
    'username': 'vagrant',
    'password': 'vagrant'
}

JINJA2_INT_TEMPLATE = "set interfaces ethernet {{ interface.name }} address '{{ interface.ip }}/{{ interface.mask }}'"
interface_template = jinja2.Template(JINJA2_INT_TEMPLATE)

num_routers_configured = 0
ips_configured = []

for router in network_data:
    num_routers_configured += 1
    print(f"\n*** Starting {router} provisioning ***")

    device_config['hostname'] = network_data[router]['mgmt_ip']
    desired_interfaces_config = network_data[router]['interfaces']

    connection = driver(**device_config)
    connection.open()

    actual_interfaces_config = connection.get_interfaces_ip()

    for interface in desired_interfaces_config:
        merge_config = ""
        ips_configured.append(interface['ip'])
        if (
            interface['name'] not in actual_interfaces_config or
            (
                interface['name'] in actual_interfaces_config and
                'ipv4' in actual_interfaces_config[interface['name']] and
                interface['ip'] not in actual_interfaces_config[interface['name']]['ipv4'] and
                int(interface['mask']) != actual_interfaces_config[interface['name']]['ipv4'][interface['ip']]
            )
        ):
            print(f"Interface {interface['name']} configuration is not ready")
            merge_config += interface_template.render(interface=interface)
        else:
            print(f"Interface {interface['name']} with IP {interface['ip']} is already ready")

    if merge_config:
        with open(PATCH_FILENAME, "w") as patch_config:
            patch_config.write(merge_config)
        res = connection.load_merge_candidate(filename=PATCH_FILENAME)
        diff = connection.compare_config()
        if diff:
            print(f"Changes to be committed:\n{diff}")
            connection.commit_config()
            print("Changes committed")
    else:
        print("No config changes detected")

    if num_routers_configured == len(network_data.keys()):
        print(f"\nAs this is the last router to provision, we will test ICMP reachability from {router}")
        for ip in ips_configured:
            pprint.pprint(connection.ping(ip))

    connection.close()

if os.path.exists(PATCH_FILENAME):
    os.remove(PATCH_FILENAME)
