from abc import ABC, abstractmethod
from dataclasses import dataclass


class Task(ABC):
    """
    The interface that defines what a task is."""

    @abstractmethod
    def execute(self):
        ...


class Task_1(Task):
    def execute(self):
        print("executing task 1")


class Task_2(Task):
    def execute(self):
        print("executing task 2")


@dataclass
class Task_3(Task):
    message: str
    loops: int

    def execute(self):
        for _ in range(1, self.loops):
            print(f" saying {self.message} {self.loops} times for task 3")


class TaskFactory(ABC):
    @abstractmethod
    def create(self) -> Task:
        pass


class Task_1Factory(TaskFactory):
    def create(self) -> Task:
        return Task_1()


class Task_2Factory(TaskFactory):
    def create(self) -> Task:
        return Task_2()


@dataclass
class Task_3Factory(TaskFactory):
    message: str
    loops: int

    def create(self) -> Task:
        return Task_3(self.message, self.loops)


class Registry:
    def __init__(self):
        self.task_registry: dict[str, TaskFactory] = {}

    def register(self, task_name: str, factory: TaskFactory) -> None:
        self.task_registry[task_name] = factory

    def unregister(self, task_name: str) -> None:
        self.task_registry.pop(task_name, None)

    def create(self, task_name: str) -> Task:
        factory = self.task_registry[task_name]
        return factory.create()

    def return_tasks(self) -> list[Task]:
        task_list = []

        for factory in self.task_registry.values():
            task = factory.create()
            task_list.append(task)

        return task_list


def main() -> None:
    registry = Registry()
    registry.register("task_1", Task_1Factory())
    registry.register("task_2", Task_2Factory())
    registry.register("task_3", Task_3Factory(message="arg to task 3", loops=5))
    print(registry.create("task_1"))
    print(registry.create("task_2"))
    print(registry.create("task_3"))

    tasks = registry.return_tasks()
    for task in tasks:
        task.execute()
    registry.unregister("product1")
    registry.unregister("product2")


if __name__ == "__main__":
    main()
