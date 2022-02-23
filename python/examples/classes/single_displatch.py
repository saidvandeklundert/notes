# multiple constructors 4:  @singledispatch or @singledispatchmethod:
from functools import singledispatchmethod
from dataclasses import dataclass


@dataclass
class HumanBuilder_1:
    name: str
    age: int


class HumanBeing:
    @singledispatchmethod
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @__init__.register(HumanBuilder_1)
    def _from_strings(self, human_builder):
        print("running init with HumanBuilder_1")
        self.name = human_builder.name
        self.age = human_builder.age

    @__init__()
    def _from_args(self, name, age):
        print("running init with HumanBuilder_1")
        self.name = name
        self.age = age


builder_1 = HumanBuilder_1(name="jan", age=6)
human_being_1 = HumanBeing(builder_1)

human_being_2 = HumanBeing(name="marie", age=3)
