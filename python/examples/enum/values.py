from enum import Enum


class Platform(Enum):
    IOS = "ios"
    IOSXR = "iosxr"
    NXOS = "nxos"
    EOS = "eos"
    JUNOS = "junos"


class SomeEnum(Enum):
    STRING = "string_value"
    DICT = {1: "one", 2: "two"}
    JUNOS = Platform.JUNOS.value
    PLATFORM = Platform


if __name__ == "__main__":
    print(SomeEnum.STRING.value)
    print(SomeEnum.DICT.value[1])

    print(SomeEnum.JUNOS)

    print(SomeEnum.PLATFORM)
