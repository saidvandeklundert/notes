from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Human:
    name: str
    age: int
    occupation: str


@dataclass
class Teacher(Human):
    name: str
    age: int
    occupation = "teacher"


class AbstractHumanFactory(ABC):
    @abstractmethod
    def get_human(self) -> Human:
        pass


class HumanFactory(AbstractHumanFactory):
    def get_human(self, name: str, age: int, occupation: str) -> Human:
        return Human(name=name, age=age, occupation=occupation)


class TeacherFactory(AbstractHumanFactory):
    def get_human(self, name: str, age: int) -> Human:
        return Human(name=name, age=age, occupation="teacher")


def read_factory(human_type: str = "base") -> HumanFactory:

    human_factories = {
        "base": HumanFactory(),
        "teacher": TeacherFactory(),
    }
    return human_factories[human_type]


if __name__ == "__main__":

    # simpl factory:
    t_factory = TeacherFactory()
    joe = t_factory.get_human(name="joe", age=32)
    print(vars(joe))
    # using read factory:
    human_factory = read_factory()
    human = human_factory.get_human("jan", 6, "jumping up and down")
    teacher_factory = read_factory("teacher")
    teacher = teacher_factory.get_human(
        "joep",
        45,
    )
    print(vars(human))
    print(vars(teacher))
