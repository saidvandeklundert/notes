import asyncio
import json
import time
from typing import List
import aiohttp
import sys
import asyncio
from json import dump

# to mitigate 'RuntimeError: Event loop is closed' on Windows
if (
    sys.version_info[0] == 3
    and sys.version_info[1] >= 8
    and sys.platform.startswith("widn")
):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def get_dev_info(session, dev):
    async with session.get(
        f"url",
        headers={
            "Authorization": "Bearer supersecret",
            "Content-Type": "application/json",
        },
        json={"title": "Try Bearer"},
    ) as resp:

        response = resp.json()
        print(response["dev_info"]["hostname"])


async def main(devices: List[str]):

    con = aiohttp.TCPConnector(ssl=False)
    async with aiohttp.ClientSession(connector=con) as session:
        tasks = []
        for dev in devices:
            task = asyncio.ensure_future(get_dev_info(session, dev))
            tasks.append(task)

        print(tasks)
        await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    devices = [
        "ss",
    ]

    loop = asyncio.get_event_loop()
    # asyncio.run(main())
    loop.run_until_complete(main(devices))
    # loop.run_until_complete(main(devices))
    # loop.close()
