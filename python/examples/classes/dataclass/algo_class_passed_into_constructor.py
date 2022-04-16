from dataclasses import dataclass
from typing import Protocol


class Algorithm(Protocol):
    def execute_algorithm(self, x: int, y: int) -> int:
        ...


@dataclass
class TaskAtHand:
    x: int
    y: int
    algorithm: Algorithm

    def run_algorithm(self) -> int:

        algo_result = self.algorithm.execute_algorithm(self.x, self.y)

        return algo_result


class Multiplier:
    def execute_algorithm(x: int, y: int) -> int:
        return x * y


class Addition:
    def execute_algorithm(x: int, y: int) -> int:
        return x + y


if __name__ == "__main__":
    task = TaskAtHand(x=4, y=4, algorithm=Multiplier)
    print(task.run_algorithm())
    task = TaskAtHand(x=4, y=4, algorithm=Addition)
    print(task.run_algorithm())
