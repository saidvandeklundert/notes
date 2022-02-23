from dataclasses import dataclass
from typing import Literal, List, Union, Optional


@dataclass
class Trunk:
    vlans: List[int]


@dataclass
class Access:

    vlan: int


@dataclass
class Interface:
    # all common properties
    name: str
    # distinguish individual subtypes:
    subtype: Union[
        Trunk,
        Access,
    ]


@dataclass
class AlternateInterface:
    name: str
    access: Optional[Access] = None
    trunk: Optional[Trunk] = None


access = Interface(name="et-0/0/1", subtype=Access(vlan=1))
trunk = Interface(name="et-0/0/1", subtype=Trunk(vlans=[1, 4, 7]))
