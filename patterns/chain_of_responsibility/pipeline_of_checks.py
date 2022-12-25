from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional, List
from dataclasses import dataclass, field


@dataclass
class CheckResult:
    name: str
    result: bool
    message: str


@dataclass
class Context:
    device_name: str
    check_results: List[CheckResult] = field(default_factory=list)


class Pipeline(ABC):
    def __init__(self, context):
        self.context: Context = context

    @abstractmethod
    def get_steps(self) -> List[Check]:
        ...

    def execute_checks(self):
        for check in self.get_steps():
            check.execute_check()

    def report(self):
        for check in self.context.check_results:
            print(
                f"\t report for {self.context.device_name}:  {check.name} {check.result}"
            )


class Check(ABC):
    def __init__(self, context: Context):
        self.context = context

    @abstractmethod
    def execute_check(self):
        ...


class BGPCheck(Check):
    def execute_check(self):
        print(f"check BGP for {self.context.device_name}")
        self.context.check_results.append(
            CheckResult(name="bgp", result=True, message="all peers are up")
        )


class InterfacesCheck(Check):
    def execute_check(self):
        print(f"check interfaces {self.context.device_name}")
        self.context.check_results.append(
            CheckResult(name="interfaces", result=True, message="all interfaces are up")
        )


class UplinkCheck(Check):
    def execute_check(self):
        print(f"check uplink for {self.context.device_name}")
        self.context.check_results.append(
            CheckResult(name="uplinks", result=False, message="all uplinks are down")
        )


class SpinePipeline(Pipeline):
    def get_steps(self) -> List[Check]:
        return [
            BGPCheck(context=self.context),
            InterfacesCheck(context=self.context),
        ]


class AccessSwitchPipeline(Pipeline):
    def get_steps(self) -> List[Check]:
        return [
            UplinkCheck(context=self.context),
            InterfacesCheck(context=self.context),
        ]


def site_check():
    devices = ["nyc1-acc-switch-101", "nyc1-spine-router-4"]
    pipelines: List[Pipeline] = []
    for device in devices:
        if "acc" in device:
            pipelines.append(AccessSwitchPipeline(context=Context(device_name=device)))
        elif "spine" in device:
            pipelines.append(SpinePipeline(context=Context(device_name=device)))

    for pipeline in pipelines:
        pipeline.execute_checks()
    for pipeline in pipelines:
        pipeline.report()


def main():
    site_check()


if __name__ == "__main__":
    main()
