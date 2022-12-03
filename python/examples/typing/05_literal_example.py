# python -m mypy .\05_literal_example.py
from dataclasses import dataclass
from typing import Literal


@dataclass
class Router:
    name: str
    vendor: Literal["Arista", "Juniper"]


r1 = Router(name="r1", vendor="Arista")

r2 = Router(name="r2", vendor="juniper")
