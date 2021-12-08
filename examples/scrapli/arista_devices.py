"""examples.async_usage.async_multiple_connections"""
import asyncio
from typing import Union
from scrapli.driver.core import AsyncEOSDriver, AsyncJunosDriver, EOSDriver

import getpass

import logging

logging.basicConfig(filename="scrapli.log", level=logging.DEBUG)
# PW = getpass.getpass()


host_list = [
    "192.168.250.32",
    # "192.168.250.33",
    # "192.168.250.34",
    # "192.168.250.35",
    # "192.168.250.36",
    # "192.168.250.37",
    # "192.168.250.38",
    # "192.168.250.39",
    # "192.168.250.40",
]

EOS = {
    "host": "",
    "auth_username": "svandeklundert",
    "auth_password": "",
    "auth_strict_key": False,
    "transport": "asyncssh",
    "driver": AsyncEOSDriver,
}

# DEVICES = [EOS_1, EOS_2,]
DEVICES = []
for host in host_list:
    addition = EOS.copy()
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


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())