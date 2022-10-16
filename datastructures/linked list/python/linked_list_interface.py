from __future__ import annotations
from abc import ABC, abstractmethod

from typing import TypeVar

T = TypeVar("T")


class LinkedList(ABC):
    @abstractmethod
    def len(
        self,
    ):
        ...

    @abstractmethod
    def insert_at(self, item: T, index: int) -> None:
        ...

    @abstractmethod
    def remove(self, item: T) -> T | None:
        ...

    @abstractmethod
    def remove_at(self, index: int) -> T | None:
        ...

    @abstractmethod
    def append(self, item: T) -> None:
        ...

    @abstractmethod
    def prepend(self, item: T) -> None:
        ...

    @abstractmethod
    def get(self, item: T) -> T | None:
        ...
