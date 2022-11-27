from dataclasses import dataclass
from typing import Protocol


class Strategy(Protocol):
    def execute(self, x: int, y: int) -> int:
        ...


@dataclass
class DataClassThatDoesTHings:
    x: int
    y: int
    strategy: Strategy

    def run_algorithm(self) -> int:
        """Runs the algorithm on the data fields in the dataclass."""
        algo_result = self.strategy.execute(self.x, self.y)

        return algo_result

    def set_algorithm(self, strategy: Strategy):
        """Change the algorithm at runtime."""
        self.strategy = strategy


class Multiplier:
    def execute(self, x: int, y: int) -> int:
        return x * y


class Addition:
    def execute(self, x: int, y: int) -> int:
        return x + y


class Subtract:
    def execute(self, x: int, y: int) -> int:
        return x - y


if __name__ == "__main__":
    task = DataClassThatDoesTHings(x=14, y=4, strategy=Multiplier())
    print(task.run_algorithm())
    task.set_algorithm(strategy=Addition())
    print(task.run_algorithm())
    task.set_algorithm(strategy=Subtract())
    print(task.run_algorithm())
