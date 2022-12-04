
[scapy github](https://github.com/secdev/scapy)
[scapy documentation](https://readthedocs.org/projects/scapy/downloads/pdf/latest/)

On the interpreter:
```python
from scapy.all import IP, ICMP, sr1 

# Specify the packet:
ip = '192.168.1.1'
icmp = IP(dst=ip)/ICMP()

# Send 1 ICMP packet:
response = sr1(icmp, timeout=5)

from scapy.all import IP, ICMP, srloop
# Send 5 ICMP packets:
response = srloop(IP(dst='192.168.1.1')/ICMP(), count=5, timeout=5)

# make it go faster:
response = srloop(IP(dst='192.168.1.1')/ICMP(), inter=0.1, count=50, timeout=5)
response[0].show()



response[0].summary()

# Check the configuration variables set by scapy:
from scapy.all import conf
conf

from scapy.all import IPv6
# make it go faster:
response = srloop(IPv6(dst='2001:4860:4860::8844')/ICMP(), inter=0.1, count=50, timeout=5)
```


```python
from scapy.all import get_windows_if_list, get_if_addr
from pprint import pprint

get_windows_if_list()
pprint(get_windows_if_list())
```

