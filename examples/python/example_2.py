import sys
from colorama import Fore, Style


input("""In this example, we will use Jinja2 templates to create and push a config to both routers.
Please, keep pressing enter to keep moving forward...""")

try:
    import netmiko
except Exception as e:
    print(f"{Fore.RED}Maybe you forgot to import Nemiko, please do 'pip3 install netmiko==2.4.2'{Style.RESET_ALL}")
    sys.exit(1)

input(f"""We will create a dictionary variable {Fore.YELLOW}base_config{Style.RESET_ALL} with the device_type, user and password.""")

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

command = "import jinja2"

exec(command)

JINJA2_TEMPLATE = "set interface ethernet {{ interface.name }} address {{ interface.ip_addr }}"

print(f"{Fore.GREEN}{JINJA2_TEMPLATE}{Style.RESET_ALL}")

input("Note the double curly brackets used to pass variables from outside")

command = 'jinja2.Template(JINJA2_TEMPLATE)'

input(f"So we instantiate a Jinja template by '{Fore.YELLOW}template = {command}{Style.RESET_ALL}'")

template = eval(command)

input("Now we are gonna iterate thorugh the source of truth to get the variables,"
      "create the specific command, and setup the config in the router")

for device in NETWORK_DEFINITION:
    input(f"Now working in {Fore.GREEN}{device}{Style.RESET_ALL}")

    input(f"Info for {Fore.GREEN}{device}: {NETWORK_DEFINITION[device]}{Style.RESET_ALL}")

    input("Now we are gonna iterate over all the interfaces")

    for interface in NETWORK_DEFINITION[device]['interfaces']:

        input(f"Now working on interface {Fore.GREEN}{interface}{Style.RESET_ALL}")

        command = 'template.render(interface=interface)'

        input(f"and now is time to apply the template to generate the config with '{Fore.YELLOW}{command}{Style.RESET_ALL}'")

        final_command = eval(command)

        print(f"{Fore.GREEN}{final_command}{Style.RESET_ALL}")

        bunch_of_commands = (
            "base_config['host'] = device\n"
            "conn = netmiko.ConnectHandler(**base_config)\n"
            "conn.config_mode()\n"
            "conn.send_command(final_command)\n"
            "conn.commit()\n"
            "conn.exit_config_mode()\n"
        )

        input(
            "Finally we push the config to the device, first adding the specific host and "
            "then connecting to the Device and sending and commiting the rendered command:\n"
            f"{Fore.YELLOW}{bunch_of_commands}{Style.RESET_ALL}"
        )

        exec(bunch_of_commands)

        command = "conn.send_command('show interfaces')"

        input(f"and we check the final output with '{Fore.YELLOW}{command}{Style.RESET_ALL}'")

        OUTPUT = eval(command)

        print(f"{Fore.GREEN}{OUTPUT}{Style.RESET_ALL}")

        command = 'conn.disconnect()'

        input(f"and when done, we disconnect from this device with '{Fore.YELLOW}{command}{Style.RESET_ALL}'")

        exec(command)

print("End of the example")
