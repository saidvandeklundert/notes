import asyncio
import aiohttp
from aiohttp import ClientSession
from util import fetch_status
from util import async_timed


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        # generate a list of URLs:
        urls = ["http://example.com" for _ in range(100)]
        # generate a list of coroutines:
        requests = [fetch_status(session, url) for url in urls]
        # pass coroutines to gather to run them concurrently:
        status_codes = await asyncio.gather(*requests)
        print(status_codes)


asyncio.run(main())