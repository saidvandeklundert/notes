import asyncio


async def coroutine():
    print("Hello world!")


if __name__ == "__main__":
    asyncio.run(coroutine())
