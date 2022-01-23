import asyncio
import aiohttp


async def get_page(session: aiohttp.ClientSession, url: str) -> str:
    """coroutine that grabs a single page"""
    async with session.get(url) as response:
        return await response.text()


async def main():
    """main coroutine"""
    async with aiohttp.ClientSession() as session:
        sites = ["http://python.org", "http://google.com", "http://yandex.ru"]
        # create a list of coroutines
        tasks = [get_page(session, url) for url in sites]
        # schudule the coroutines to run:
        results = await asyncio.gather(*tasks, return_exceptions=True)
        # filter the successes and the exceptions:
        exceptions = [result for result in results if isinstance(result, Exception)]
        successes = [result for result in results if not isinstance(result, Exception)]
        # print some information:
        print(f"{len(exceptions)} failed and {len(successes)} completed")
        for page in successes:
            print(page[0:100])


if __name__ == "__main__":
    from sys import platform

    if "win" in platform:
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
