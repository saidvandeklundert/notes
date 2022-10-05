from enum import Enum
from pydantic import BaseModel, ValidationError, validator
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
    """
    >>> import uuid
    >>> from network.network_service.network import Device
    >>> Device(**{'id': 'ac591eeb-c963-435f-9e22-08242dbb53d6', 'name': 'r10', 'os': Os.JUNOS,'vendor': Vendor.JUNIPER})
    """

    id: str = str(uuid.uuid4())
    name: str
    os: Os
    vendor: Vendor

    @validator("id")
    def username_alphanumeric(cls, v):
        assert isinstance(uuid.UUID(v), uuid.UUID), "must be a valid UUID"
        return v


class Devices(BaseModel):
    devices: list[Device]
