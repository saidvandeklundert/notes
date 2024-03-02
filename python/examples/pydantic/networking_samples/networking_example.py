from pydantic import BaseModel
from enum import Enum, auto
import ipaddress
from typing import Union
import json

class Os(Enum):
    JUNOS = "JUNOS"
    EOS = "EOS"
    IOSXE = "IOSXE"

class Role(Enum):
    FW = "FW"
    CORE_ROUTER = "CORE_ROUTER"
    TOR = "TOR"






class Interface(BaseModel):
    description: str
    address: Union[ipaddress.IPv4Interface, ipaddress.IPv6Interface]



class Router(BaseModel):
    hostname: str
    vendor: Os
    interfaces: list[Interface] = []

    role:Role
    
    class Config:  
        use_enum_values = True 

if __name__ == "__main__":
    print("yolo")
    r1 = Router(hostname="cr.sjc.01", vendor=Os.JUNOS, role=Role.CORE_ROUTER,interfaces=[Interface(description="some description",address="1.1.1.1/24")])



    print(r1)
    print("role", r1.role)
    print(r1.model_dump_json(indent=2))

    r2 = Router(**json.loads("""
{
  "hostname": "cr.tor.2",
  "vendor": "IOSXE",
  "interfaces": [
    {
      "description": "some description",
      "address": "192.168.0.1/24"
    }
  ],
  "role": "TOR"
}"""))
    # typos
    Router(**json.loads("""
{
  "hostname": "cr.tor.2",
  "vendor": "IOSXEEE",
  "interfaces": [
    {
      "description": "some description",
      "address": "192.168.0.1/24"
    }
  ],
  "role": "TOR"
}"""))
    r2.json
    
    Router(**json.loads("""
{
  "hostname": "cr.tor.2",
  "vendor": "IOSXEEE",
  "interfaces": [
    {
      "description": "some description",
      "address": "192.168.0.1.1/24"
    }
  ],
  "role": "TOR"
}"""))