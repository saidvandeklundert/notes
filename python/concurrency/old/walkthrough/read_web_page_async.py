import asyncio
import aiohttp
from sys import platform
from datetime import datetime

if "win" in platform:
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


def read_urls() -> list[str]:
    """Read URLs form a file and return them
    as a list."""
    with open("url_list.txt", "r") as f:
        urls = f.readlines()
    urls = [url.strip() for url in urls]
    return urls


async def get_page(session: aiohttp.ClientSession, url: str) -> str:
    """coroutine that grabs a single page"""
    async with session.get(url) as response:
        return await response.text()


async def main():
    """main coroutine"""
    async with aiohttp.ClientSession(read_timeout=4) as session:

        # create a list of coroutines
        tasks = [get_page(session, url) for url in read_urls()]
        # schedule the coroutines to run:
        results = await asyncio.gather(*tasks, return_exceptions=True)
        # filter the successes and the exceptions:
        exceptions = [result for result in results if isinstance(result, Exception)]
        successes = [result for result in results if not isinstance(result, Exception)]
        # print some information:
        for page in successes:
            print(page[0:10])

        print(f"{len(exceptions)} failed and {len(successes)} completed")


if __name__ == "__main__":

    startTime = datetime.now()
    asyncio.run(main())
    duration = datetime.now() - startTime
    print(f"script took {duration}")
    # script took 0:00:05.312448
