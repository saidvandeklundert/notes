import itertools
import asyncio


async def spin(msg: str) -> None:
    for char in itertools.cycle(r"\|/-"):
        status = f"\r{char} {msg}"
        print(status, flush=True, end="")
        try:
            await asyncio.sleep(0.1)
        except asyncio.CancelledError:
            break
    blanks = " " * len(status)
    print(f"\r{blanks}\r", end="")


async def slow() -> int:
    await asyncio.sleep(3)
    return 42


async def supervisor() -> int:
    spinner = asyncio.create_task(spin("thinking!"))
    print(f"spinner object: {spinner}")
    result = await slow()
    spinner.cancel()
    return result


def main() -> None:
    result = asyncio.run(supervisor())
    print(f"Answer: {result}")


if __name__ == "__main__":
    main()
