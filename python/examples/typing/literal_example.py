# mypy.exe .\example.py
from dataclasses import dataclass
from typing import Literal


@dataclass
class Router:
    name: str
    vendor: Literal["Arista", "Juniper"]


r1 = Router(name="r1", vendor="Arista")
