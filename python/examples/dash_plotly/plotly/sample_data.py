from pydantic import BaseModel


class Region(BaseModel):
    name: str
    count: int


region_data = [
    Region(name="tok", count=100),
    Region(name="ams", count=2039),
    Region(name="fra", count=244),
    Region(name="dub", count=3434),
    Region(name="dal", count=3456),
]
