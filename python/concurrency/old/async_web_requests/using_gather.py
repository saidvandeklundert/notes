import asyncio
from asyncio import exceptions
import aiohttp
from util import async_timed
from util import fetch_status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        urls = ["https://example.com", "python://example.com"]
        tasks = [fetch_status(session, url) for url in urls]
        results = await asyncio.gather(*tasks, return_exceptions=True)

        exception_results = [res for res in results if isinstance(res, Exception)]
        successful_results = [res for res in results if not isinstance(res, Exception)]

        print(f"All results: {results}")
        print(f"Finished succesfully: {successful_results}")
        print(f"Threw exceptions: {exception_results}")


asyncio.run(main())