import sys
from colorama import Fore, Style


input("""In this example, we will explore Netmiko library to connect and configure a device programmatically.
Please, keep pressing enter to move forward.""")

command = 'import netmiko'
try:
    exec(command)
except Exception as e:
    print(f"{Fore.RED}Maybe you forgot to import Nemiko, please do it 'pip3 install netmiko'{Style.RESET_ALL}")
    sys.exit(1)

input(f"Netmiko module imported by doing '{Fore.YELLOW}{command}{Style.RESET_ALL}'")

command = 'dir(netmiko)'

input(f"Let's explore what is available within the library by running '{Fore.YELLOW}{command}{Style.RESET_ALL}'")

NETMIKO_OPTIONS = eval(command)

print(f"{Fore.GREEN}{NETMIKO_OPTIONS}{Style.RESET_ALL}")

input("See the ConnectHandler class, it's an object that will enable us to connect to a device")

input("""This class needs some information to setup the connection, in this case we will provide:
* device_type: it specifies the type of device to connect
* host: FQDN to connect or IP
* username: username used to connect
* password: password used to connect""")

input(f"""We will create a dictionary variable '{Fore.YELLOW}CONFIG{Style.RESET_ALL}' with the basic information""")

CONFIG = {
    'device_type': 'vyos',
    'host': 'routerA',
    'username': 'vagrant',
    'password': 'vagrant'
}

print(f"{Fore.GREEN}{CONFIG}{Style.RESET_ALL}")

command = 'netmiko.ConnectHandler(**CONFIG)'

input(f"and then, we instantiate a variable of the class, '{Fore.YELLOW}conn = {command}{Style.RESET_ALL}")

conn = eval(command)

input("Finally, we are connected to the device, so we are ready to interact with it")

raw_cmd_show_interfaces = 'show interfaces'

command = f"conn.send_command('{raw_cmd_show_interfaces}')"

input(f"First, let's to a simple '{raw_cmd_show_interfaces}' command with '{Fore.YELLOW}{command}{Style.RESET_ALL}'")

OUTPUT = eval(command)

print(f"{Fore.GREEN}{OUTPUT}{Style.RESET_ALL}")

command = 'conn.config_mode()'

input(f"We can enter config mode with '{Fore.YELLOW}{command}{Style.RESET_ALL}'")

exec(command)

commands = """conn.send_command('set interface ethernet eth2 address 192.0.2.100/24')
conn.commit()"""

input(f"and now let's configure an IP on eth2 with send_command and commit it:\n'{Fore.YELLOW}{commands}{Style.RESET_ALL}'")

exec(commands)

command = "conn.exit_config_mode()"

input(f"Let's back to the operational mode with '{Fore.YELLOW}{command}{Style.RESET_ALL}'")

exec(command)

command = f"conn.send_command('{raw_cmd_show_interfaces}')"

input(f"and check the interfaces again with '{Fore.YELLOW}{command}{Style.RESET_ALL}'")

OUTPUT = eval(command)

print(f"{Fore.GREEN}{OUTPUT}{Style.RESET_ALL}")

input("Here we can observe the recently assigned IP address")

print("End of the example")
