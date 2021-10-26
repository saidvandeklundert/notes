"""
Following creates 3 coroutines which are passed into 'as_completed'.

This will wrap the coroutines in tasks and run them.

As they finish, the result is returned and we can do stuff with it.
"""
import asyncio
import aiohttp
from util import async_timed, fetch_status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = [
            fetch_status(session, "https://www.example.com", 1),
            fetch_status(session, "https://www.example.com", 1),
            fetch_status(session, "python://www.example.com", 1),
            fetch_status(session, "https://www.example.com", 10),
        ]

        for finished_task in asyncio.as_completed(fetchers):
            try:
                print(await finished_task)
            except Exception as err:
                print("Error", err)


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())