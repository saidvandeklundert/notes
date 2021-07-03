from typing import List
from pydantic import BaseModel


class Interface(BaseModel):
    name: str
    speed_gbps: int


class Router(BaseModel):
    hostname: str
    vendor: str
    model: str
    interfaces: List[Interface]


spine02 = {
    "hostname": "spine02",
    "vendor": "juniper",
    "model": "qfx10k",
    "interfaces": [
        {
            "name": "et-0/0/0",
            "speed_gbps": 100,
        },
        {
            "name": "et-0/0/1",
            "speed_gbps": 100,
        },
    ],
}

if __name__ == "__main__":
    int_1 = Interface(name="Et1", speed_gbps=100)
    int_2 = Interface(name="Et2", speed_gbps=100)
    spine01 = Router(
        hostname="spine01",
        vendor="Arista",
        model="whatgives",
        interfaces=[int_1, int_2],
    )
    spine01 = Router(**spine02)
    print(spine01)
    print(spine02)
