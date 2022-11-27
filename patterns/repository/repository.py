from abc import ABC, abstractmethod
from repository_model import Task


class Repository(ABC):
    @abstractmethod
    def create(self, task: Task) -> Task:
        ...

    @abstractmethod
    def read(self, task: Task) -> Task:
        ...

    @abstractmethod
    def update(self, task: Task):
        ...

    @abstractmethod
    def delete(self, task: Task):
        ...
