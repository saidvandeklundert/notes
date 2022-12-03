from abc import ABC, abstractmethod
from repository_model import Task
import uuid


class Repository(ABC):
    @abstractmethod
    def create(self, task: Task) -> None:
        ...

    @abstractmethod
    def read(self, task_id: uuid.UUID) -> Task:
        ...

    @abstractmethod
    def update(self, task: Task) -> None:
        ...

    @abstractmethod
    def delete(self, task: Task) -> None:
        ...

    @abstractmethod
    def load(self) -> list[Task]:
        ...
