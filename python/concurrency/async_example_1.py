import asyncio
import time
import aiohttp


async def download_site(session, url):
    async with session.get(url) as response:
        print(f"{url} status {response.status}")


async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site(session, url))
            tasks.append(task)

        await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    sites = [
        "https://www.nu.nl",
        "http://google.nl",
    ] * 10

    start = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(download_all_sites(sites))
    print(f"Touched {len(sites)} sites in {time.time() - start} seconds")