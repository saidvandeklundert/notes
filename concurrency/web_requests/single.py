import asyncio
import aiohttp
from aiohttp import ClientSession
from util import async_timed


@async_timed()
async def fetch_status(session: ClientSession, url: str) -> int:
    ten_millis = aiohttp.ClientTimeout(total=0.1)

    async with session.get(url, timeout=ten_millis) as result:
        return result.status


@async_timed()
async def main():
    # use the async context manager to open a ClientSession that can then be used
    #  to make subsequent requests for different URLs.
    async with aiohttp.ClientSession() as session:
        url = "http://www.google.com"
        status = await fetch_status(session, url)
        print(f"Status for {url} was {status}.")


asyncio.run(main())
