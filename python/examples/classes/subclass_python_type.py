# Built-in namespace
import builtins


# Extended subclass
class mystr(str):
    def first_last(self):
        if self:
            return self[0] + self[-1]
        else:
            return ""


# Substitute the original str with the subclass on the built-in namespace
builtins.str = mystr
print(mystr(123).first_last())

output = """
14
00

Traceback (most recent call last):
  File "strp.py", line 16, in <module>
    print '0'.first_last()
AttributeError: 'str' object has no attribute 'first_last'
"""


class Dict(dict):
    @property
    def easyaccess(self):
        return self.__getitem__("1").get("1")


d = Dict({"1": {"1": "a"}})

print(d.easyaccess)
print(d["1"])
