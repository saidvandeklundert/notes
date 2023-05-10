from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty


class Check(ABC):
    @abstractmethod
    def execute_check():
        ...


class CheckPipeline(ABC):
    @abstractmethod
    def get_checks() -> list[Check]:
        ...

    def execute_steps(self):
        for step in self.get_checks():
            step.execute_check()


class UpLoadSoftwareToDevice(Check):
    def __init__(self, context):
        self.context = context

    def execute_check(self):
        for device in self.context["devices"]:
            print(f"uploading software for {device}")


class CreateBackup(Check):
    def __init__(self, context):
        self.context = context

    def execute_check(self):
        for device in self.context["devices"]:
            print(f"creating a backup for {device}")


class PreChecks(Check):
    def __init__(self, context):
        self.context = context

    def execute_check(self):
        for device in self.context["devices"]:
            print(f"running prechecks for {device}")


class Upgrade(Check):
    def __init__(self, context):
        self.context = context

    def execute_check(self):
        for device in self.context["devices"]:
            print(f"performing upgrade for {device}")


class PostChecks(Check):
    def __init__(self, context):
        self.context = context

    def execute_check(self):
        for device in self.context["devices"]:
            print(f"running post check for {device}")


class PipelineLAN(CheckPipeline):
    def __init__(self, context):
        self.context = context

    def get_checks(self):
        return [
            UpLoadSoftwareToDevice(context=self.context),
            CreateBackup(context=self.context),
            PostChecks(context=self.context),
            Upgrade(context=self.context),
            PostChecks(context=self.context),
        ]

    def execute_steps(self):
        for step in self.get_checks():
            step.execute_step()


if __name__ == "__main__":
    context = {
        "devices": [
            "r1",
            "r2",
        ]
    }
    wf = PipelineLAN(context)
    wf.execute_steps()
