from dataclasses import dataclass
from typing import Callable


@dataclass
class TaskAtHand:
    x: int
    y: int
    task: Callable

    def execute_callable(self) -> int:
        task_result = self.task(self.x, self.y)
        return task_result


def multiply(x: int, y: int) -> int:
    return x * y


def add(x: int, y: int) -> int:
    return x + y


if __name__ == "__main__":
    task = TaskAtHand(x=4, y=4, task=multiply)
    print(task.execute_callable())
    task = TaskAtHand(x=4, y=4, task=add)
    print(task.execute_callable())
