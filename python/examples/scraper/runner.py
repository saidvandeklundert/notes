"""
Run some tasks
"""
from tasks import add, check_site, hello, scrape
import yaml
import ipaddress


def list_all_targets() -> list[str]:
    targets = []
    with open("subnets.yaml", "rt") as f:
        ip_networks = yaml.safe_load(f)

    for ip_network in ip_networks:

        for ip_address in ipaddress.IPv4Network(ip_network):
            targets.append(ip_address)
    return targets


for ip in list_all_targets():
    val = str(ip)
    result = scrape.delay(val)
    res = result.get(timeout=1)
    print(res)

for _ in range(0, 100):
    result = hello.delay()
    result.ready()
    res = result.get(timeout=1)
    print(res)

for x in range(0, 80):
    result = add.delay(4, x)
    result.ready()
    res = result.get(timeout=1)
    print(res)

sites = [
    "http://nu.nl",
    "http://google.nl",
]
for url in sites:
    result = check_site.delay(url)
    res = result.get(timeout=1)
    print(res)

#
