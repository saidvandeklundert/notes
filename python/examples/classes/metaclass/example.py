"""
Metaclass example where we take the base 'type' and extend the
 constructor.
"""


class AttributeInitType(type):
    def __call__(self, *args, **kwargs):
        """Create a new instance."""

        # First, create the object in the normal default way.
        obj = type.__call__(self, *args)

        # Additionally, set attributes on the new object.
        for name, value in kwargs.items():
            setattr(obj, name, value)

        # Return the new object.
        return obj


class Human(object, metaclass=AttributeInitType):
    """
    We can initialze an instance of this class with any amount of fields.

    Additionally, the description property will display all fields that were
    added to the class.

    Effectively, we changed the behavior of the base class."""

    @property
    def description(self) -> str:
        """Return a description of this car."""
        return " ".join(str(value) for value in self.__dict__.values())


if __name__ == "__main__":
    joe = Human(name="Joe", age=24, profession="bum")
    print(vars(joe))
    print(joe.description)
