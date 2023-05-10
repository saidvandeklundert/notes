import asyncio
import aiohttp
from aiohttp import ClientSession
from util import async_timed, fetch_status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = [
            fetch_status(session, "https://example.com"),
            fetch_status(session, "https://example.com"),
        ]

        done, pending = await asyncio.wait(fetchers)

        print(f"Done task count {len(done)}")
        print(f"Pending task count: {len(pending)}")

        for done_task in done:
            result = await done_task
            print(result)


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())