from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty


class Step(ABC):
    @abstractmethod
    def execute_step():
        ...


class UpLoadSoftwareToDevice(Step):
    def __init__(self, context):
        self.context = context

    def execute_step(self):
        for device in self.context["devices"]:
            print(f"uploading software for {device}")


class CreateBackup(Step):
    def __init__(self, context):
        self.context = context

    def execute_step(self):
        for device in self.context["devices"]:
            print(f"creating a backup for {device}")


class PreChecks(Step):
    def __init__(self, context):
        self.context = context

    def execute_step(self):
        for device in self.context["devices"]:
            print(f"running prechecks for {device}")


class Upgrade(Step):
    def __init__(self, context):
        self.context = context

    def execute_step(self):
        for device in self.context["devices"]:
            print(f"performing upgrade for {device}")


class PostChecks(Step):
    def __init__(self, context):
        self.context = context

    def execute_step(self):
        for device in self.context["devices"]:
            print(f"running post check for {device}")


class WorkFlow:
    def __init__(self, context):
        self.context = context

    def get_steps(self):
        return [
            UpLoadSoftwareToDevice(context=self.context),
            CreateBackup(context=self.context),
            PostChecks(context=self.context),
            Upgrade(context=self.context),
            PostChecks(context=self.context),
        ]

    def execute_steps(self):
        for step in self.get_steps():
            step.execute_step()


if __name__ == "__main__":

    context = {
        "devices": [
            "r1",
            "r2",
        ]
    }
    wf = WorkFlow(context)
    wf.execute_steps()
