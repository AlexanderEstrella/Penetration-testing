import socket
import requests
import psutil  # Import the psutil module

# Getting the hostname by socket.gethostname() method
hostname = socket.gethostname()

# Getting all IP addresses associated with all network adapters
ip_addresses = []
for interface, addrs in psutil.net_if_addrs().items():
    for addr_info in addrs:
        if addr_info.family == socket.AF_INET:
            ip_addresses.append(addr_info.address)

# Printing the hostname and all IP addresses
print(f"Hostname: {hostname}")
print("IP Addresses:")
for ip in ip_addresses:
    print(ip)

# Make an HTTP GET request to get your public IP address
try:
    response = requests.get('https://api.ipify.org')
    if response.status_code == 200:
        public_ip = response.text
        print('My public IP address is:', public_ip)
    else:
        print('Failed to retrieve public IP address.')
except requests.exceptions.RequestException as e:
    print('An error occurred while making the request:', e)

input('Press ENTER to exit')
