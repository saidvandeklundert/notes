import asyncio
import aiohttp
from aiohttp import ClientSession
from util import async_timed


async def fetch_status(session: ClientSession, url: str, delay: int = 1) -> int:
    await asyncio.sleep(delay)
    async with session.get(url, timeout=3000) as result:
        x = result.status
        print(await result.text())

        return x


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        # generate a list of URLs:
        urls = ["http://example.com" for _ in range(100)]
        # generate a list of coroutines:
        requests = [fetch_status(session, url) for url in urls]
        # pass coroutines to gather to run them concurrently:
        status_codes = await asyncio.gather(*requests, return_exceptions=True)
        ## Gather does some 'magic' to return the results in the order they were made.
        print(status_codes)


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())