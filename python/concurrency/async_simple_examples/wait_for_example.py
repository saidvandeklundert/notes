import asyncio
import datetime


def print_now() -> None:
    print(f"{datetime.datetime.now()}")


async def keep_printing(name: str = "") -> None:
    while True:
        print(name)
        print_now()
        await asyncio.sleep(1)


async def main() -> None:
    """wrap the gather in a wait_for to ensure it stops running after 6 seconds."""
    await asyncio.wait_for(asyncio.gather(keep_printing("jan")), 6)


if __name__ == "__main__":
    asyncio.run(main())