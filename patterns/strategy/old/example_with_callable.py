"""
Strategy pattern example:
- each algorithm is defined as a function
- the algorithms can be passed into a class that is performing a task

This is also displaying 'dependancy inversion'.

The class that is performing the task is not depending on any concrete algorithm.

The dependancy is inverted since the function is defined outside of
the task and it is passed into the task object.
"""


"""
Three algorithms are defined:
"""
from typing import Callable


def multiply(x, y):
    return x * y


def add(x, y):
    return x + y


def something_complicated(x, y):
    return x + y * (x + y)


"""
The class that can execute a variety of algorithms:
"""
from dataclasses import dataclass


@dataclass
class Executor:
    x: int
    y: int
    algorithm: Callable

    def execute(self) -> int:
        """Execute an injected callable."""
        algorithm_result = self.algorithm(self.x, self.y)
        return algorithm_result


if __name__ == "__main__":
    """
    In the following examples, the client (Executor) will run 3 different
     algorithms.
    """
    # multiply example:
    example_1 = Executor(x=4, y=4, algorithm=multiply)
    print(example_1.execute())
    # add example:
    example_2 = Executor(x=4, y=4, algorithm=add)
    print(example_2.execute())
    # something_complicated example:
    example_3 = Executor(x=4, y=4, algorithm=something_complicated)
    print(example_3.execute())
