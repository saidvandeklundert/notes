from enum import Enum


class Vendor(str, Enum):
    JUNIPER = "juniper"
    CISCO = "cisco"
    ARISTA = "arista"


class VendorNoStr(Enum):
    JUNIPER = "juniper"
    CISCO = "cisco"
    ARISTA = "arista"


"""
In [11]: "juniper" == Vendor.JUNIPER
Out[11]: True

In [12]: "juniper" == VendorNoStr.JUNIPER
Out[12]: False

In [14]: Vendor.JUNIPER[1::]
Out[14]: 'uniper'

In [15]: VendorNoStr.JUNIPER[1::]
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Input In [15], in <cell line: 1>()
----> 1 VendorNoStr.JUNIPER[1::]

TypeError: 'VendorNoStr' object is not subscriptable
"""
