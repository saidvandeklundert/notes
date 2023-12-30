import ipaddress

#

ipaddress.ip_network('192.168.0.16/28').overlaps(ipaddress.ip_network('192.168.0.0/24'))  

#
a_list_of_networks = [
    ipaddress.IPv4Network("1.0.0.0/8"),
    ipaddress.IPv4Network("1.0.0.0/14"),
    ipaddress.IPv4Network("1.0.0.0/16"),
    ipaddress.IPv4Network("1.0.0.0/23"),
    ipaddress.IPv4Network("1.0.0.0/24"),
    ipaddress.IPv4Network("1.0.0.0/25"),
    ipaddress.IPv4Network("1.0.0.0/27"),
]

for network in a_list_of_networks:
    overlap = ipaddress.ip_network(network).overlaps(ipaddress.ip_network("1.0.0.0/32"))
    if overlap is True:
        print(f"{network} overlaps with 1.0.0.0/32")


for network in a_list_of_networks:
    overlap = ipaddress.ip_network(network).overlaps(ipaddress.ip_network("1.100.0.0/32"))
    if overlap is True:
        print(f"{network} overlaps with 1.100.0.0/32")
       

def check_network_member_ship(network_1, network_2)->bool:
    """
    Check if network_2 is in network_1.
    """
    overlap = ipaddress.ip_network(network_1).overlaps(ipaddress.ip_network(network_2))
    if overlap is True:
        print(f"{network_2} is in  {network_1}")    
    return overlap

check_network_member_ship("1.0.0.0/24", "2.2.2.2/32")
check_network_member_ship("1.0.0.0/24", "1.0.0.2/32")


# from so
import socket,struct

def makeMask(n):
    "return a mask of n bits as a long integer"
    return (2<<n-1) - 1

def dottedQuadToNum(ip):
    "convert decimal dotted quad string to long integer"
    return struct.unpack('L',socket.inet_aton(ip))[0]

def networkMask(ip,bits):
    "Convert a network address to a long integer" 
    return dottedQuadToNum(ip) & makeMask(bits)

def addressInNetwork(ip,net):
   "Is an address in a network"
   return ip & net == net

address = dottedQuadToNum("192.168.1.1")
networka = networkMask("10.0.0.0",24)
networkb = networkMask("192.168.0.0",24)
print(address,networka,networkb)
print(addressInNetwork(address,networka))
print(addressInNetwork(address,networkb))