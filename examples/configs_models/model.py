from pydantic import BaseModel
from typing import List, Union, Dict
from enum import Enum
from typing import Optional
import yaml
import ipaddress


class Layer3SubInterface(BaseModel):
    """Subinterface that can be assigned a VRF"""

    description: Optional[str]
    vrf: Optional[str]
    ipv4: Optional[ipaddress.IPv4Interface]
    ipv6: Optional[ipaddress.IPv6Interface]


class Target(BaseModel):
    """route-target community"""

    target: str

    class Config:
        allow_mutation = False


class Layer3Vpn(BaseModel):
    """Layer 3 virtual network"""

    name: str
    target_import: List[Target]
    target_export: List[Target]
    vn_interfaces: List[Layer3SubInterface] = []

    class Config:
        allow_mutation = False


if __name__ == "__main__":
    """examples where the models are built"""
    target = Target(
        **yaml.safe_load(
            """
---
target: "45001:2"
"""
        )
    )
    print(target.json(indent=2))
    vpn_example = Layer3Vpn(
        **yaml.safe_load(
            """
---
name: INTERNET
target_import:
  - target: "1:1"
  - target: "2:2"
  - target: "3:3"  
target_export:
  - target: "1:1"
  - target: "2:2"
"""
        )
    )
    print(vpn_example.json(indent=2))
    sub_interface = Layer3SubInterface(
        **yaml.safe_load(
            """
---
description: "customer 1"
vrf: "vrf1"
ipv4: "10.0.0.1/31"
ipv6: "2001:db8::1/127"
"""
        )
    )
    print(sub_interface.json(indent=2))
