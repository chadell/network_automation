import sys
from colorama import Fore, Style


input("""In this example, we will explore the Napalm library and see what abstract methods it exposes.
Please, keep pressing enter to keep moving forward.""")

command = "import napalm"

try:
    exec(command)
except Exception as e:
    print(f"{Fore.RED}Maybe you forgot to {command}, please do 'pip3 install napalm-vyos'{Style.RESET_ALL}")
    sys.exit(1)

command = "dir(napalm)"

input(f"First, let's check the Napalm library with '{Fore.YELLOW}{command}{Style.RESET_ALL}'")

NAPALM_OPTIONS = eval(command)

print(f"{Fore.GREEN}{NAPALM_OPTIONS}{Style.RESET_ALL}")

command = "napalm.get_network_driver('vyos')"

input(f"Now, we first load the proper device driver, with '{Fore.YELLOW}{command}{Style.RESET_ALL}'")

driver = eval(command)

input("and from the driver, we instantiate a device, with our custom config")

CONFIG = {
    'hostname': 'routerA',
    'username': 'vagrant',
    'password': 'vagrant'
}

print(f"{Fore.GREEN}{CONFIG}{Style.RESET_ALL}")

command = "device = driver(**CONFIG)"

input(f"and then, we instantiate a device connection '{Fore.YELLOW}{command}{Style.RESET_ALL}'")

exec(command)

command = "device.open()"

input(f"finally, we open the connection with the device with '{Fore.YELLOW}{command}{Style.RESET_ALL}'")

exec(command)

command = "dir(device)"

input(f"So, finally we will see the capabilities Napalm is abstracting to us with '{Fore.YELLOW}{command}{Style.RESET_ALL}'")

NAPALM_ABSTRACT_METHODS = eval(command)

print(f"{Fore.GREEN}{NAPALM_ABSTRACT_METHODS}{Style.RESET_ALL}")

command = 'device.get_interfaces_ip()'

input(f"Let's try the get_interfaces_ip: '{Fore.YELLOW}{command}{Style.RESET_ALL}'")

INTERFACE_INFO = eval(command)

print(f"{Fore.GREEN}{INTERFACE_INFO}{Style.RESET_ALL}")

command = "device.ping('192.168.0.101')"

input(f"We can even try a ping with '{Fore.YELLOW}{command}{Style.RESET_ALL}'")

result = eval(command)

print(f"{Fore.GREEN}{result}{Style.RESET_ALL}")

print("End of the example")
