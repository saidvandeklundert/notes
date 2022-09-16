from enum import Enum
from pydantic import BaseModel
import uuid


class Os(str, Enum):
    IOS = "ios"
    IOSXR = "iosxr"
    NXOS = "nxos"
    EOS = "eos"
    JUNOS = "junos"


class Vendor(str, Enum):
    JUNIPER = "juniper"
    CISCO = "cisco"
    ARISTA = "arista"


class Device(BaseModel):
    id: uuid.UUID = uuid.uuid4()
    name: str
    os: Os
    vendor: Vendor


class Devices(BaseModel):
    devices: list[Device]
