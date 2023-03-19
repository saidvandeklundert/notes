from __future__ import annotations
from pydantic import BaseModel
from enum import Enum
from typing import Optional
from dataclasses import dataclass


class Vendor(Enum):
    CISCO = "cisco"
    ARISTA = "arista"
    JUNIPER = "juniper"


class NetworkDevice(BaseModel):
    name: str
    vendor: Vendor
    interfaces: list[Interface] = []


class Interface(BaseModel):
    name: str
    description: str
    enabled: bool


class InterfacesList(BaseModel):
    interfaces: list[Interface] = []


if __name__ == "__main__":
    dev_1 = NetworkDevice(
        name="R1",
        vendor=Vendor.CISCO,
    )
    dev_2 = NetworkDevice(
        name="R2",
        vendor=Vendor.JUNIPER,
    )

    print(dev_1, dev_2)

    interface_1 = Interface(
        name="GigabitEthernet0/0", description="to R2", enabled=True
    )
    interface_2 = Interface(
        name="ge-0/0/0",
        description="to R1",
        enabled=True,
    )
    interfaces_list_r1_r2 = InterfacesList(interfaces=[interface_1, interface_2])
