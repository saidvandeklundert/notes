import asyncio
import logging
import aiohttp
from util import async_timed, fetch_status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        good_request = fetch_status(session, "https://www.example.com")
        bad_request = fetch_status(session, "python://www.example.com")

        fetchers = [asyncio.create_task(good_request), asyncio.create_task(bad_request)]

        done, pending = await asyncio.wait(fetchers)

        print(f"Done, task count: {len(done)}")
        print(f"Pending task count: {len(pending)}")

        for done_task in done:
            if done_task.exception() is None:
                print(done_task.result())
            else:
                logging.error(
                    "Request got an exception", exc_info=done_task.exception()
                )


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())
