import asyncio
import functools
import time
from typing import Callable, Any
import aiohttp
from aiohttp import ClientSession


def async_timed():
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapped(*args, **kwargs) -> Any:
            print(f"starting {func} with args {args} and kwargs {kwargs}")
            start = time.time()
            try:
                return await func(*args, **kwargs)
            finally:
                end = time.time()
                total = end - start
                print(f"finished {func} in {total:.4f} second(s)")

        return wrapped

    return wrapper


async def delay(delay_seconds: int) -> int:
    print(f"Sleeping for {delay_seconds} seconds.")
    await asyncio.sleep(delay_seconds)
    print(f"finished sleeping for {delay_seconds} second(s)")
    return delay_seconds


@async_timed()
async def fetch_status(session: ClientSession, url: str, delay: int = 1) -> int:
    await asyncio.sleep(delay)
    async with session.get(url, timeout=3000) as result:
        return result.status
