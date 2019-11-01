import sys
from colorama import Fore, Style


input("""In this example, we will explore Netmiko library to connect and configure
a device programmatically.
Please, keep pressing any key to move forward.""")

try:
    import netmiko
except Exception as e:
    print(f"{Fore.RED}Maybe you forgot to import Nemiko, please do 'pip3 install netmiko'{Style.RESET_ALL}")
    sys.exit(1)

print(f"{Fore.GREEN}Netmiko module imported{Style.RESET_ALL}")
input("Let's explore what is available within the library...")
NETMIKO_OPTIONS = dir(netmiko)
print(f"{Fore.GREEN}{NETMIKO_OPTIONS}{Style.RESET_ALL}")
input("See the ConnectHandler class, it's an object that will enable us to connect to a device")

input("""This class needs some information to setup the connection, in this case we will provide:
* device_type: it specifies the type of device to connect
* host: FQDN to connect or IP
* username: username used to connect
* password: password used to connect""")
input("""We will create a dictionary variable (CONFIG) with all this information""")
CONFIG = {
    'device_type': 'vyos',
    'host': 'routerA',
    'username': 'vagrant',
    'password': 'vagrant'
}
print(f"{Fore.GREEN}{CONFIG}{Style.RESET_ALL}")
input("and then, we instantiate a variable of the class, conn = netmiko.ConnectHandler(**CONFIG)")
conn = netmiko.ConnectHandler(**CONFIG)
input("Finally, we are connected to the device, so we are ready to interact with the device")

input("First, let's to a simple 'show interfaces' command with 'conn.send_command('show interfaces')'")
OUTPUT = conn.send_command('show interfaces')
print(f"{Fore.GREEN}{OUTPUT}{Style.RESET_ALL}")
input("We can enter config mode with 'conn.config_mode()'")
conn.config_mode()
input("and now let's configure an IP on eth2 with send_command and commit it")
conn.send_command('set interface ethernet eth2 address 172.26.0.111/24')
conn.commit()
input("Let's back to the operational mode")
conn.exit_config_mode()
input("Let's check the interfaces again")
OUTPUT = conn.send_command('show interfaces')
print(f"{Fore.GREEN}{OUTPUT}{Style.RESET_ALL}")
print("End of the example")
