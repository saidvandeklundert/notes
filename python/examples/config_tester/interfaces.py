from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
import tests_cisco_system
import functools


class Test(ABC):
    @abstractmethod
    def run_tests(self) -> None:
        """Execute a test or a series of tests"""
        ...


class TestSequence(ABC):
    def __init__(self, context):
        self.context = context

    @abstractmethod
    def get_steps(self) -> List[Test]:
        ...

    def execute_steps(self):
        for step in self.get_steps():
            step.run_tests()


class TestContext:
    def __init__(self, hostname: str, configuration: str):
        self.hostname = hostname
        self.configuration = configuration

    @functools.cached_property
    def configuration_lines(self) -> List[str]:
        return [line.strip() for line in self.configuration]
