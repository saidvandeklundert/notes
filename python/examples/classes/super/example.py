class PersonParent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Here I am again in the parent with ID: {id(self)}")


class Person(PersonParent):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Initializing myself with ID: {id(self)}")
        super(Person, self).__init__(name, age)


if __name__ == "__main__":
    jan = Person("jan", 6)
