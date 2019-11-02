import sys
from colorama import Fore, Style


input("""In this example, we will explore the Napalm library and see what abstract methods it exposes.
Please, keep pressing any key to move forward.""")

try:
    import napalm
except Exception as e:
    print(f"{Fore.RED}Maybe you forgot to import Napalm, please do 'pip3 install napalm-vyos'{Style.RESET_ALL}")
    sys.exit(1)

input("First, let's check the Napalm library")
NAPALM_OPTIONS = dir(napalm)
print(f"{Fore.GREEN}{NAPALM_OPTIONS}{Style.RESET_ALL}")

input("Now, we first load the proper device driver, with 'napalm.get_network_driver('vyos')'")
driver = napalm.get_network_driver("vyos")
input("and from the driver, we instantiate a device, with our custom config")
CONFIG = {
    'hostname': 'routerA',
    'username': 'vagrant',
    'password': 'vagrant'
}
print(f"{Fore.GREEN}{CONFIG}{Style.RESET_ALL}")
input("and then, we instantiate a device connection 'device = driver(**CONFIG)'")
device = driver(**CONFIG)
input("finally, we open the connection with the device with 'device.open()'")
device.open()

input("So, finally we will see the capabilities Napalm is abstracting to us...")
NAPALM_ABSTRACT_METHODS = dir(device)
print(f"{Fore.GREEN}{NAPALM_ABSTRACT_METHODS}{Style.RESET_ALL}")

input("Let's try the get_interfaces_ip: 'device.get_interfaces_ip()'")
INTERFACE_INFO = device.get_interfaces_ip()
print(f"{Fore.GREEN}{INTERFACE_INFO}{Style.RESET_ALL}")

input("We can even try a ping with 'device.ping('192.168.0.101')'")
device.ping('192.168.0.101')

print("End of the example")
