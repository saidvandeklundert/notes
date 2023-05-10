import asyncio
import json
import time

import aiohttp


async def worker(name, n, session):
    print(f"Worker {name} starting it's thing.")
    url = f"http://qrng.anu.edu.au/API/jsonI.php?length={n}&type=uint16"
    response = await session.request(method="GET", url=url)
    value = await response.json()
    return value


async def main():
    async with aiohttp.ClientSession() as session:
        response = await worker("Dave", 3, session)
        print(response["data"])
    async with aiohttp.ClientSession() as session:
        responses = await asyncio.gather(
            *(worker(f"worker-nr-{i}", n, session) for i, n in enumerate(range(1, 10)))
        )
        for response in responses:
            print(response["data"])


if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - start
    print(f"Done in {elapsed:0.2f} seconds.")