from dataclasses import dataclass
from typing import Optional, List
from ipaddress import IPv4Address, IPv6Address


@dataclass
class Interface:
    name: str
    ipv4: Optional[IPv4Address] = None
    ipv6: Optional[IPv6Address] = None


@dataclass
class Router:
    interfaces: List[Interface]


r1 = Router(
    interfaces=[
        Interface(name="et-0/0/0", ipv4="1.1.1.1/30"),
        Interface(name="et-0/0/1", ipv4="1.1.1.5/30"),
        Interface(name="et-0/0/2", ipv4="1.1.1.9/30"),
        Interface(name="et-0/0/3", ipv4="1.1.1.13/30"),
    ]
)


try:
    for interface in r1:
        print(interface)
except TypeError as err:
    print(err)


@dataclass
class RouterNg:
    interfaces: List[Interface]

    def __iter__(self):  # implements iterator protocol for RouterNg
        return iter(self.interfaces)


r1_ng = RouterNg(
    interfaces=[
        Interface(name="et-0/0/0", ipv4="1.1.1.1/30"),
        Interface(name="et-0/0/1", ipv4="1.1.1.5/30"),
        Interface(name="et-0/0/2", ipv4="1.1.1.9/30"),
        Interface(name="et-0/0/3", ipv4="1.1.1.13/30"),
        Interface(name="et-0/0/4", ipv6="2001:db8::0/127"),
        Interface(name="et-0/0/5", ipv6="2001:db8::2/127"),
        Interface(name="et-0/0/6", ipv6="2001:db8::4/127"),
        Interface(name="et-0/0/7", ipv6="2001:db8::6/127"),
        Interface(name="et-0/0/8", ipv6="2001:db8::8/127"),
    ]
)

# we can now iterate the class:
for interface in r1_ng:
    print(interface)

iterator = r1_ng.__iter__()
iterator.__next__()
iterator.__next__()
iterator.__next__()  # eventually, you run into 'StopIteration'


# we can also use list comprehensions:
only_ipv4 = [x for x in r1_ng if x.ipv4]
only_ipv6 = [x for x in r1_ng if x.ipv6]


# dot operator:
r1_ng.interfaces[0].name
r1_ng.interfaces[0].ipv4
r1_ng.interfaces[0].ipv6
r1_ng.interfaces[4].name
r1_ng.interfaces[4].ipv4
r1_ng.interfaces[4].ipv6
