# python -m mypy .\03_dataclass.py
from dataclasses import dataclass


@dataclass
class Router:
    name: str
    uptime_seconds: int
    live: bool


router_correct = Router(name="r1", uptime_seconds=20, live=True)

router_oops = Router(name="r1", uptime_seconds="20", live=True)

# think about the cases where you use a class that:
# - is imported
# - has 5 or more fields
