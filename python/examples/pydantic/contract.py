import yaml
from pydantic import BaseModel
from typing import Union


class BgpParameters(BaseModel):
    local_asn: int
    local_oob_asn: int
    ibgp_hold_time: int
    ebgp_hold_time: int


yaml_str = """
local_asn: 65000
local_oob_asn: 65001
ibgp_hold_time: 90
ebgp_hold_time: 90
"""

bgp_parameters = BgpParameters(**yaml.safe_load(yaml_str))


yaml_str_err = """
local_asn: 65000
local_oob_asn: 65001
ibgp_hold_time: 90
"""

bgp_parameters = BgpParameters(**yaml.safe_load(yaml_str_err))
