from typing import List
import asyncio
import time
import aiohttp
from os import getenv

from aiohttp.client import ClientSession


API_KEY = getenv("API_KEY")


async def api_call(session: ClientSession, url: str):
    """coroutine that uses aiohttp to make an API call"""
    headers = {
        "Authorization": f"{API_KEY}",
        "Content-Type": "application/json",
    }
    async with session.get(
        url, headers=headers, json={"title": "Try Bearer"}
    ) as response:
        print(f"{url} status {response.status}")
        print("Content-type:", response.headers["content-type"])
        json_respone = await response.json()
        print(json_respone)


async def main(sites: List[str]):
    """main entry point for running api calls asynchronously"""
    # disable aiohttp ssl verification
    con = aiohttp.TCPConnector(ssl=False)
    # open async context manager
    async with aiohttp.ClientSession(connector=con) as session:
        print(f"\n\n\nUSING ensure_future:\n" + (30 * "=") + "\n\n\n")
        # start adding tasks using ensure future:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(api_call(session, url))
            tasks.append(task)

        # run all tasks:
        await asyncio.gather(*tasks, return_exceptions=True)
        print(f"\n\n\nUSING create_task:\n" + (30 * "=") + "\n\n\n")
        # alternatively, create tasks using create_task:
        alt_tasks = [asyncio.create_task(api_call(session, url)) for url in sites]
        # run all tasks:
        await asyncio.gather(*alt_tasks, return_exceptions=True)


if __name__ == "__main__":
    sites_list: List[str] = [
        "http://httpbin.org/anything",
    ] * 20  # 00

    start = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(sites_list))
    print(f"Touched {len(sites_list)} sites in {time.time() - start} seconds")