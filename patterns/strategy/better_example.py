"""
Strategy pattern example:
- each algorithm is put into it's own class
- the algorithms can be passed into a class that is performing a task

This is also displaying 'dependancy inversion'.

The class that is performing the task is not depending on any concrete algorithm.

The dependancy is inverted since the algorithm is constructed outside of
the task and it is passed into the task object.
"""


"""
Three algorithms are defined:
"""

from abc import ABC, abstractmethod


class Algorithm(ABC):
    @abstractmethod
    def run_algorithm(self, x, y) -> int:
        pass


class Multiply(Algorithm):
    def run_algorithm(self, x, y) -> int:
        return x * y


class Add(Algorithm):
    def run_algorithm(self, x, y) -> int:
        return x + y


class SomethingMoreComplex(Algorithm):
    def run_algorithm(self, x, y) -> int:
        return x + y * (x + y)


"""
The class that can execute a variety of algorithms:
"""
from dataclasses import dataclass


@dataclass
class Executor:
    x: int
    y: int
    algorithm: Algorithm

    def execute(self) -> int:
        """Execute an injected algorithm that satisfies the
        'Algorithm' protocol."""
        algorithm_result = self.algorithm.run_algorithm(self.x, self.y)
        return algorithm_result


if __name__ == "__main__":
    """
    In the following examples, the client (Executor) will run 3 different
     algorithms.
    """
    # Multiply example:
    example_1 = Executor(x=4, y=4, algorithm=Multiply())
    print(example_1.execute())
    # Addition example:
    example_2 = Executor(x=4, y=4, algorithm=Add())
    print(example_2.execute())
    # SomethingMoreComplex example:
    example_3 = Executor(x=4, y=4, algorithm=SomethingMoreComplex())
    print(example_3.execute())
