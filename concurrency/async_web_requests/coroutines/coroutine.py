# from https://realpython.com/async-io-python/
#!/usr/bin/env python3
# countasync.py

import asyncio


async def count():
    print("One")
    await asyncio.sleep(3)
    print("Two")


async def main():
    tasks = [count() for x in range(100)]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    import time

    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")