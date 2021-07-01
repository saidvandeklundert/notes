# https://docs.python.org/3/library/enum.html
from enum import Enum


class Platform(str, Enum):
    IOS = "ios"
    IOSXR = "iosxr"
    NXOS = "nxos"
    EOS = "eos"
    JUNOS = "junos"


if __name__ == "__main__":
    for p in Platform:
        print(p)
        print(p.name)
    print(Platform.EOS.name)
    print(Platform.EOS.value)