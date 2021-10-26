import asyncio
import aiohttp
from util import async_timed, fetch_status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = [
            fetch_status(session, "https://example.com", 0),
            fetch_status(session, "https://example.com", 10),
            fetch_status(session, "https://example.com", 10),
        ]

    for done_task in asyncio.as_completed(fetchers, timeout=3):
        try:
            result = await done_task
            print("done, got this:\n")
            print(result)
        except Exception:
            print("We got a timeout")
    for task in asyncio.tasks.all_tasks():
        print(task)


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

asyncio.run(main())