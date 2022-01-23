"""
@property is a decorator that you can use to decorate methods in classes.

After a method is decorated with @property, it can be accessed as an attribute:

```
class Human:
    def __init__(self, name: str):
        self._name = name

    @property
    def name(self):
        return self._name
marie = Human("marie")
marie.name
```

Notice the last statement, it is not written 'marie.name()', like a normal method.

After using @property on name, you can no longer change the name in the way you would change an attribute.

In order to change or delete the property, you need to use a 'getter' or a 'setter'. These come with their own syntax.

In the above example, it would be as follows:
```
    @name.setter
    def fullname(self, name: str):
        self.name = name

    @name.deleter
    def fullname(self):
        del self.name
```

"""


class Human:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"{self.name}"


class OtherHuman:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    @property
    def fullname(self):
        """This can be accessed as an attribute."""
        return f"{self.name} {self.surname}"

    @fullname.setter
    def fullname(self, fullname: str):
        name, surname = fullname.split(" ", 1)
        self.name = name
        self.surname = surname

    @fullname.deleter
    def fullname(self):
        del self.name
        del self.surname

    def __repr__(self):
        return f"{self.fullname}"


if __name__ == "__main__":
    jan = Human("jan")
    print(jan)

    jan.name = "somethingelse"
    print(jan)

    marie = OtherHuman("Marie", "van de Klundert")
    print(marie)
    print(marie.fullname)
    marie.fullname = "Jan van de Klundert"
    print(marie)
    print(marie.fullname)

    # another example
    class Example:
        def __init__(self, example) -> None:
            self.example = example

        @property
        def example(self):
            return self._example

        @example.setter
        def example(self, value):
            if not isinstance(value, str):
                raise ValueError("this is not a string")
            self._example = value

    # Here we enforce some construction logic
    # it must be a string in this case, but you can do anything you want really.
    example = Example("example")
    print(example.example)