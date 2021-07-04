import asyncio
import aiosnmp
import os

"""
		".1.3.6.1.2.1.1.1.0",
		"1.3.6.1.2.1.1.5.0",
"""
hosts = [line.rstrip() for line in open("hosts.txt")]
# export SNMP_STRING=xxx
SNMP_STRING = os.getenv("SNMP_STRING")


async def async_snmp(host):
    print("async snmp")
    try:
        async with aiosnmp.Snmp(
            host=host, port=161, community=SNMP_STRING, timeout=1
        ) as snmp:
            for res in await snmp.get(".1.3.6.1.2.1.1.1.0"):
                print(res.oid, res.value)
    except Exception as err:
        print(f"{err} touching {host}")


async def main():
    async with aiosnmp.Snmp(
        host=hosts[2], port=161, community=SNMP_STRING, timeout=2
    ) as snmp:
        for res in await snmp.get(".1.3.6.1.2.1.1.1.0"):
            print(res.oid, res.value)
    async with aiosnmp.Snmp(
        host="1.1.1.1", port=161, community=SNMP_STRING, timeout=1
    ) as snmp:
        try:
            for res in await snmp.get(".1.3.6.1.2.1.1.1.0"):
                print(res.oid, res.value)
        except:
            pass
    await asyncio.gather(*(async_snmp(host) for host in hosts))


if __name__ == "__main__":
    asyncio.run(main())