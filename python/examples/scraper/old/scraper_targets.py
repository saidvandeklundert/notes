import ipaddress
import queue
import yaml

AddressQueue = queue.Queue()

with open("subnets.yaml", "rt") as f:
    ip_networks = yaml.safe_load(f)

for ip_network in ip_networks:

    for ip_address in ipaddress.IPv4Network(ip_network):
        AddressQueue.put(ip_address)
AddressQueue.put(None)
print(AddressQueue)

for job in iter(AddressQueue.get, None):
    print(job)
