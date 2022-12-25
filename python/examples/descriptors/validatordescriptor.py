from typing import Callable, Any


def below_4097(x: int):
    """Example func to be passed into the Validation class
    that is part of the Field descriptor."""
    if x < 4097:
        return True
    else:
        return False


def not_0_or_below_0(x: int):
    """Example func to be passed into the Validation class
    that is part of the Field descriptor."""
    if x >= 0:
        return True
    else:
        return False


class Validation:
    def __init__(
        self, validation_function: Callable[[Any], bool], error_msg: str
    ) -> None:
        self.validation_function = validation_function
        self.error_msg = error_msg

    def __call__(self, value):
        # run the validation function and raise and error
        # if the return is False.
        if not self.validation_function(value):
            raise ValueError(f"{value!r} {self.error_msg}")


class Field:
    """
    Descriptor that runs a validator everytime a field
    is set to a value.

    The Field class is instantiated with 1 or more Validator
    instances.
    """

    def __init__(self, *validations):
        self._name = None
        self.validations: tuple[Validation] = validations

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self._name]

    def validate(self, value):
        for validation in self.validations:
            validation(value)

    def __set__(self, instance, value):
        self.validate(value)
        instance.__dict__[self._name] = value


class ClientClass:
    descriptor = Field(
        Validation(lambda x: isinstance(x, (int, float)), "is not a number"),
        Validation(not_0_or_below_0, "is not >= 0"),
        Validation(below_4097, "needs to be below 4097"),
    )


if __name__ == "__main__":
    client = ClientClass()
    client.descriptor = 42
    client.descriptor
    # >>> 42
    client.descriptor = 90900
    client.descriptor = -42
    # >>>Traceback
