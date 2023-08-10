from __future__ import annotations
from pydantic import BaseModel
from enum import Enum, auto


class OperationSelector(Enum):
    PRE_CHANGE_DATA_COLLECTION = auto()
    POST_CHANGE_DATA_COLLECTION = auto()
    PRE_POST_CHANGE_DATA_COMPARISON = auto()
    SHIFT_TRAFFIC = auto()
    CERTIFY_NETWORK = auto()
    HIGH_SEV = auto()


class Platform(Enum):
    IOS = "IOS"
    JUNOS = "JUNOS"


class NetworkVerifySelector(BaseModel):
    operation: OperationSelector = OperationSelector.CERTIFY_NETWORK
    role: str = "default"
    platform: Platform

    def get_pipeline(self):
        return PIPELINE_MAP[self.platform][(self.role, self.operation)]


juniper_default_pipeline = ["chassis alarms"]
cisco_default_pipeline = ["show ip int brief"]
cisco_spine_pipeline = ["show ip int brief", "show ip bgp summary"]

JUNOS_PIPELINE_MAP = {
    "default": juniper_default_pipeline,
}

IOS_PIPELINE_MAP = {
    "default": cisco_default_pipeline,
    "spine": cisco_spine_pipeline,
}

PIPELINE_MAP = {
    Platform.IOS: IOS_PIPELINE_MAP,
    Platform.JUNOS: JUNOS_PIPELINE_MAP,
}


if __name__ == "__main__":
    selector = NetworkVerifySelector(
        operation=OperationSelector.CERTIFY_NETWORK, role="spine", platform=Platform.IOS
    )
    print(selector.get_pipeline())
