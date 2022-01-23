import asyncio
import datetime


def print_now() -> None:
    print(f"{datetime.datetime.now()}")


async def keep_printing(name: str = "") -> None:
    """This is a trampoline"""
    while True:
        print(f"{name}")
        print_now()
        await asyncio.sleep(1)


if __name__ == "__main__":
    coroutine = keep_printing("Hello")
    print(type(keep_printing))  # <class 'function'>
    print(type(coroutine))  # <class 'coroutine'>
    # start the event loop and run the trampoline:
    asyncio.run(keep_printing(name="Jan"))

"""
>>> import asyncio
>>> loop.run_until_complete(asyncio.sleep(5))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'loop' is not defined
>>> asyncio.get_event_loop()
<ProactorEventLoop running=False closed=False debug=False>
>>> loop
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'loop' is not defined
>>> loop = _
>>> loop.run_forever() # run the loop foverever
KeyboardInterrupt
>>> loop
<ProactorEventLoop running=False closed=False debug=False>
>>> loop.run_until_complete(asyncio.sleep(5))
import datetime
def print_now():
    print(datetime.datetime.now())
>>> loop.call_soon(print_now)
<Handle print_now() at <stdin>:1>
>>> loop.call_soon(print_now)
<Handle print_now() at <stdin>:1>
>>> loop.run_until_complete(asyncio.sleep(5))
2021-10-28 11:41:58.705383
2021-10-28 11:41:58.706464
"""