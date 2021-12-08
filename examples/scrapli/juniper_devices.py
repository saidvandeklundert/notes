"""examples.async_usage.async_multiple_connections"""
import asyncio
from scrapli.driver.core import AsyncEOSDriver, AsyncJunosDriver
import logging

logging.basicConfig(filename="scrapli.log", level=logging.DEBUG)
import getpass

# PW = getpass.getpass()

host_list = [
    "10.0.13.135",
    "10.0.13.136",
    "10.0.13.137",
    "10.0.13.138",
    "10.0.13.163",
    "10.0.13.164",
    "10.0.13.99",
    "10.0.13.100",
    "10.0.13.101",
    "10.0.13.102",
    "10.0.13.53",
    "10.0.13.54",
    "10.0.13.253",
    "10.0.13.254",
    "10.0.14.27",
    "10.0.14.28",
    "10.0.14.29",
    "10.0.14.30",
]
JUNOS = {
    "host": "10.0.21.233",
    "auth_username": "svandeklundert",
    "auth_password": "",
    "auth_strict_key": False,
    "transport": "asyncssh",
    "driver": AsyncJunosDriver,
}


DEVICES = []
for host in host_list:
    addition = JUNOS.copy()
    addition["host"] = host
    DEVICES.append(addition)


async def gather_version(device):
    """Simple function to open a connection and get some data"""
    driver = device.pop("driver")
    conn = driver(**device)
    await conn.open()
    prompt_result = await conn.get_prompt()
    version_result = await conn.send_command("show version")
    await conn.close()
    return prompt_result, version_result


async def main():
    """Function to gather coroutines, await them and print results"""
    coroutines = [gather_version(device) for device in DEVICES]
    results = await asyncio.gather(*coroutines)
    for result in results:
        print(f"device prompt: {result[0]}")
        print(f"device show version: {result[1].result}")
    import pdb

    pdb.set_trace()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())