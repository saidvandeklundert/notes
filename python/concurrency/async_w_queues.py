"""
Pizza pipeline

3 queueus and the end result is a list of pizzas
"""
from typing import List
import asyncio
import random
import time
import itertools


async def randsleep(caller: str) -> None:
    i = random.randint(0, 3)
    if caller:
        print(f"{caller} sleeping for {i} seconds")
    await asyncio.sleep(i)


async def randsleep_topper(caller: str) -> None:
    i = random.randint(0, 3)
    if caller:
        print(f"\t{caller} sleeping for {i} seconds")
    await asyncio.sleep(i)


async def randsleep_oven(caller: str) -> None:
    i = random.randint(0, 3)
    if caller:
        print(f"\t\t{caller} sleeping for {i} seconds")
    await asyncio.sleep(i)


async def prepare_dough(caller: str) -> str:
    i = random.randint(0, 3)
    print(f"{caller} is making dough, will take {i} seconds")
    await asyncio.sleep(i)
    return f"dough from {caller}"


async def prepare_topping(caller: str, dough: str) -> str:
    i = random.randint(0, 3)
    print(f"\t{caller} is putting toppings in place, will take {i} seconds")
    await asyncio.sleep(i)
    return f"<{dough}> with toppings from {caller}"


async def dough_chef(name: str, q: asyncio.Queue) -> None:
    for _ in itertools.repeat(None, 8):
        d = await prepare_dough(name)
        t = time.perf_counter()
        await q.put((d, t))
        print(f"dough chef {name} added <{d}> to queue.")


async def topping_chef(
    name: str, dough_queue: asyncio.Queue, topping_queue: asyncio.Queue
) -> None:
    while True:
        await randsleep_topper(caller=name)

        dough, t = await dough_queue.get()
        topping = await prepare_topping(name, dough)
        now = time.perf_counter()
        print(
            f"\ttopping chef {name} got <{dough}> from queue and made <{topping}>, took {int(now - t)} seconds."
        )
        dough_queue.task_done()
        await topping_queue.put((topping, t))


async def oven_chef(
    name: str, topping_queue: asyncio.Queue, pizza_list: List[str]
) -> None:
    while True:
        await randsleep_oven(caller=name)

        pizza, t = await topping_queue.get()

        now = time.perf_counter()
        print(
            f"\t\toven chef {name} got <{pizza}> from the queue and put it in the oven, took {int(now - t)} seconds."
        )
        pizza_list.append(f"{pizza} baked by {name}")
        topping_queue.task_done()


async def main():
    FINISHED_PIZZA = []
    dough_queue = asyncio.Queue()
    topping_queue = asyncio.Queue()
    dough_chefs = [
        asyncio.create_task(dough_chef(name, dough_queue))
        for name in ["Joe", "Jason", "John", "Johnny"]
    ]
    topping_chefs = [
        asyncio.create_task(topping_chef(name, dough_queue, topping_queue))
        for name in [
            "Sue",
            "Suzie",
            "Suzzanne",
        ]
    ]
    oven_chefs = [
        asyncio.create_task(oven_chef(name, topping_queue, FINISHED_PIZZA))
        for name in [
            "Smokey",
            "Smokes",
            "Smoker",
        ]
    ]

    await asyncio.gather(*dough_chefs)
    await dough_queue.join()
    await topping_queue.join()
    for tc in topping_chefs:
        tc.cancel()
    for oc in oven_chefs:
        oc.cancel()
    print("PIPELINE FINISHED!\n===============================\n\n")
    for pizza in FINISHED_PIZZA:
        print(pizza)


if __name__ == "__main__":
    asyncio.run(main())
