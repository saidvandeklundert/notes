import time
import asyncio


async def io_bound_function(p1: int, p2: int):
    """
    Simulates an IO-bound function using asyncio.sleep(2).
    """
    print(f"io_bound_function called with arguments {p1} and {p2}")
    await asyncio.sleep(2)
    print(f"io_bound_function with arguments {p1} and {p2} ended")


async def main():
    start = time.perf_counter()
    arguments = [(x, x + 3) for x in range(10)]
    await asyncio.gather(*(io_bound_function(*arg) for arg in arguments))
    elapsed = time.perf_counter() - start
    print(f"took {elapsed:0.2f} seconds.")


if __name__ == "__main__":
    asyncio.run(main())
