import ipaddress

network = ipaddress.IPv4Network("1.0.0.0/24")



# Test address membership:

ipaddresses = [
    ipaddress.IPv4Address("1.0.1.1"),
    ipaddress.IPv4Address("1.0.0.1"),
    ipaddress.IPv4Address("1.0.0.105"),
    ipaddress.IPv4Address("2.0.0.1"),          
]

for address in ipaddresses:
    if address in network:
        print(f"{address} is in {network}")



