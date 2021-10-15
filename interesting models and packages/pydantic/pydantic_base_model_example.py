from typing import Optional, Union
from pydantic import BaseModel

import ipaddress
from profiling_deco import time_func, profile_func


class BgpPeering(BaseModel):
    """BGP peering model to define a single BGP session."""

    vrf: Optional[str]
    source: Union[ipaddress.IPv4Interface, ipaddress.IPv6Interface]
    destination: Union[ipaddress.IPv4Interface, ipaddress.IPv6Interface]
    neighbor_as: str
    source_as: str

    class Config:
        allow_mutation = False


BGP_D = {
    "vrf": "TESTING",
    "source": "172.16.1.1",
    "destination": "172.16.10.1",
    "neighbor_as": "65000",
    "source_as": "65001",
}


@profile_func
# @time_func
def create_peering():
    x = BgpPeering(**BGP_D)


if __name__ == "__main__":
    create_peering()