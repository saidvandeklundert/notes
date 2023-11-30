from pydantic import BaseModel, ValidationError, validator
import json


class Vlan(BaseModel):
    name: str
    id: int

    @validator("id")
    def vlan_validator(cls, v):
        assert v >= 1, "invalid vlan number, number too low"
        assert v <= 4094, "invalid vlan number, number too high"
        return v

    @validator("name")
    def name_validator(cls, v):
        assert len(v) >= 2, "Name length too short"
        assert len(v) <= 10, "Name length too long"
        return v


if __name__ == "__main__":
    working = Vlan(**json.loads('{"name":"PROD","id":[]}'))
    
    Vlan(**json.loads('{"name":"PROD","id":5000}'))
    Vlan(**json.loads('{"name":"THIS_NAME_IS_TOO_LONG","id":2}'))