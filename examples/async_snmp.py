import asyncio
import aiosnmp
import os

"""
	
		".1.3.6.1.2.1.1.1.0",
		"1.3.6.1.2.1.1.5.0",
"""

# export SNMP_STRING=xxx
SNMP_STRING = os.getenv("SNMP_STRING")


async def main():
    async with aiosnmp.Snmp(
        host="10.198.137.68", port=161, community=SNMP_STRING
    ) as snmp:
        for res in await snmp.get(".1.3.6.1.2.1.1.1.0"):
            print(res.oid, res.value)


asyncio.run(main())