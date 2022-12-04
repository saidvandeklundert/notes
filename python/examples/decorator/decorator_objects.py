"""
Stacking decorators that use nested functions can become cumbersome to maintain 
 and read. For one, stacking them is ugly. But perhaps the bigger disadvantage is
 that those stacked decorator functions do not have state.

A nicer implementation that removes the use of many different decorators
 would be to se a class that defines the decorator.

We can pass all the parameters in the __init__ method and implemnt the decorator
 logic on the __call__ method.
"""

import functools
import time
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


class DecoratorObject:
    """
    A decorator in the form of a class.

    This class
    """

    def __init__(
        self,
        first_message: str = "first message",
        second_message: str = "second message",
    ) -> None:
        self.first_message = first_message
        self.second_message = second_message

    def some_method(self):
        print("leveraging the state in the object")
        print(self.first_message)
        print(self.second_message)

    def __call__(self, operation):
        @functools.wraps(operation)
        def wrapped(*args, **kwargs):
            """
            The decorator function that:
            - calls a class method
            - logs a message
            - records the start time
            - runs the decorated thing
            - logs the time it took to run the decorated thing
            - returns the result that the decorated function produced
            """
            self.some_method()
            logger.info(f"'wrapped' is going to run '{operation.__name__}'")
            start_time = time.perf_counter()
            value = operation(*args, **kwargs)
            end_time = time.perf_counter()
            logger.info(
                f"completed '{operation.__name__}' in {end_time - start_time:.2f} secs"
            )
            return value

        return wrapped


@DecoratorObject()
def some_task(num_times):
    for num in range(num_times):
        sum([i ** 2 for i in range(10000)])
        print(num)


some_task(2)


@DecoratorObject(first_message="MESSAGE 1", second_message="MESSAGE 2")
def some_other_task(num_times):
    for num in range(num_times):
        sum([i ** 2 for i in range(10000)])
        print(num)


some_other_task(4)
