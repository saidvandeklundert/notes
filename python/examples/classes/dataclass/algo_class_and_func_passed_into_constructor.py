from dataclasses import dataclass
from typing import Callable, Protocol


class Algorithm(Protocol):
    def execute_algorithm(self, x: int, y: int) -> int:
        ...


@dataclass
class TaskAtHand:
    x: int
    y: int
    task: Callable
    algorithm: Algorithm

    def execute_task_and_algorithm(self) -> int:
        task_result = self.task(self.x, self.y)
        algo_result = self.algorithm.execute_algorithm(self.x, self.y)
        print(f"task_result {task_result} algo_result {algo_result}")
        return task_result + algo_result


def multiply(x: int, y: int) -> int:
    return x * y


def add(x: int, y: int) -> int:
    return x + y


class Multiplier:
    def execute_algorithm(x: int, y: int) -> int:
        return x * y


class Addition:
    def execute_algorithm(x: int, y: int) -> int:
        return x + y


if __name__ == "__main__":
    task = TaskAtHand(x=4, y=4, task=multiply, algorithm=Multiplier)
    print(task.execute_task_and_algorithm())
    task = TaskAtHand(x=4, y=4, task=add, algorithm=Addition)
    print(task.execute_task_and_algorithm())
