import sys
from colorama import Fore, Style
import json
import pprint


input("""In this example, we will understand the basic differences between YAML, JSON and XML formats.
Please, keep pressing enter to keep moving forward...""")

try:
    import yaml
except Exception as e:
    print(f"{Fore.RED}Maybe you forgot to import yaml, please do 'pip3 install pyyaml'{Style.RESET_ALL}")
    sys.exit(1)

try:
    import dicttoxml
    from xml.dom.minidom import parseString
except Exception as e:
    print(f"{Fore.RED}Maybe you forgot to import dicttoxml, please do 'pip3 install dicttoxml'{Style.RESET_ALL}")
    sys.exit(1)


example = {
    "key1": "value1",
    "key2": ["value2_1", "value2_2"],
    "key3": {
        "value3_key": "value3_value"
    }
}

input(f"\nFirst, let's explore the native Python dictionary.")
print(f"{Fore.GREEN}{example}{Style.RESET_ALL}")

input(f"\nNow, time to check YAML encoding\n")
print(f"{Fore.GREEN}{yaml.dump(example)}{Style.RESET_ALL}")

input(f"\nNow, time to check JSON encoding\n")
print(f"{Fore.GREEN}{json.dumps(example, indent=4)}{Style.RESET_ALL}")

input(f"\nNow, time to check XML encoding\n")
xml = dicttoxml.dicttoxml(example)
dom = parseString(xml)
print(f"{Fore.GREEN}{dom.toprettyxml()}{Style.RESET_ALL}")

print("\nEnd of the example")
