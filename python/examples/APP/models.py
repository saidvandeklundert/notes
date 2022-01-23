from typing import List
from dataclasses import dataclass



@dataclass
class Vlan:
    id: int
    description: str


v_one = Vlan(id=1, description="null")
v_six = Vlan(id=6, description="staging")
