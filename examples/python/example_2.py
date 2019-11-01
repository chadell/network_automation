import sys
from colorama import Fore, Style


input("""In this example, we will use Jinja2 templates to create and push a config to both routers.
Please, keep pressing any key to move forward.""")

try:
    import netmiko
except Exception as e:
    print(f"{Fore.RED}Maybe you forgot to import Nemiko, please do 'pip3 install netmiko'{Style.RESET_ALL}")
    sys.exit(1)


input("""We will create a dictionary variable base_config with the device_type, user and password.""")
base_config = {
    'device_type': 'vyos',
    'username': 'vagrant',
    'password': 'vagrant'
}
print(f"{Fore.GREEN}{base_config}{Style.RESET_ALL}")
input("""Note that we don't define the host, as we will use the same for both routers""")

input("""Now, we create our network abstract definition, this could be seen as a simple source of truth""")
NETWORK_DEFINITION = {
    'routerA': {
        'interfaces': [
            {
                'name': 'eth2',
                'ip_addr': '192.0.2.1/24'
            }
        ]
    },
    'routerB': {
        'interfaces': [
            {
                'name': 'eth2',
                'ip_addr': '192.0.2.2/24'
            }
        ]
    }
}
print(f"{Fore.GREEN}{NETWORK_DEFINITION}{Style.RESET_ALL}")

input("Now we are gonna define a Jinja2 template that will be used to setup the " \
      "config from the source of truth")
import jinja2
JINJA2_TEMPLATE = "set interface ethernet {{ interface.name }} address {{ interface.ip_addr }}"
print(f"{Fore.GREEN}{JINJA2_TEMPLATE}{Style.RESET_ALL}")
input("Note the double curly brackets used to pass variables from outside")
template = jinja2.Template(JINJA2_TEMPLATE)

input("""Now we are gonna iterate thorugh the source of truth to get the variables,
create the specific command, and setup the config in the router""")

for device in NETWORK_DEFINITION:
    input(f"Now working in {Fore.GREEN}{device}{Style.RESET_ALL}")
    input(f"Info for {Fore.GREEN}{device}: {NETWORK_DEFINITION[device]}{Style.RESET_ALL}")
    input("Now we are gonna iterate over all the interfaces")
    for interface in NETWORK_DEFINITION[device]['interfaces']:
        input(f"Now working in interface {Fore.GREEN}{interface}{Style.RESET_ALL}")
        input("and now is time to apply the template to generate the config")
        command = template.render(interface=interface)
        print(f"{Fore.GREEN}{command}{Style.RESET_ALL}")
        input("Finally we push the config to the device, first adding the specific host...")
        base_config['host'] = device
        conn = netmiko.ConnectHandler(**base_config)
        conn.config_mode()
        conn.send_command(command)
        conn.commit()
        conn.exit_config_mode()
        input("and we check the final output")
        OUTPUT = conn.send_command('show interfaces')
        print(f"{Fore.GREEN}{OUTPUT}{Style.RESET_ALL}")
        conn.disconnect()
print("End of the example")
