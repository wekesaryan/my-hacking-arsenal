# Unix/Linux system MAC_changer

import subprocess
import re


def get_interfaces():
    # Retrieve a list of available network interfaces.
    try:
        output = subprocess.check_output(["ifconfig"]).decode("utf-8")
        interfaces = re.findall(r"^\w+", output, re.MULTILINE)
        return interfaces
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while retrieving interfaces: {e}")
        return []


# Display available interfaces
interfaces = get_interfaces()
if not interfaces:
    print("No network interfaces found. Exiting.")
    exit()

print("Available network interfaces:")
for i, iface in enumerate(interfaces, start=1):
    print(f"{i}. {iface}")

# Let the user select an interface
try:
    choice = int(input("Select an interface by typing the number: "))
    if choice < 1 or choice > len(interfaces):
        print("Invalid choice. Exiting.")
        exit()
    interface = interfaces[choice - 1]
except ValueError:
    print("Invalid input. Please enter a number. Exiting.")
    exit()

# Get the new MAC address
new_mac = input("Enter the new MAC address: ")

try:
    # Change the MAC address
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

    # Verify the change
    output = subprocess.check_output(["ifconfig", interface]).decode("utf-8")
    changed_mac = re.search(r"([0-9A-Fa-f]{2}(:[0-9A-Fa-f]{2}){5})", output)

    if changed_mac and changed_mac.group(0).lower() == new_mac.lower():
        print("MAC address was successfully changed to", new_mac)
    else:
        print("Failed to change the MAC address.")
except subprocess.CalledProcessError as e:
    print(f"An error occurred while executing a command: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
