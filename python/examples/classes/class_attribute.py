class Human:
    # class attribute:
    population: int = 0

    @classmethod
    def display_population(cls):
        return f"Current population is {cls.population}"

    @classmethod
    def alternate_constructor(cls, data: dict):
        """Construct an instance of the class using alternate input,
        in this case a dictionary."""
        return cls(data["name"])

    def __init__(self, name: str):
        self.name = name
        # increment the class attribute for every new Human:
        Human.population += 1

    def __del__(self):
        # decrement class attribute automatically:
        Human.population -= 1


print(Human.display_population())
jan = Human("jan")
print(Human.display_population())
marie = Human("marie")
print(Human.display_population())
del marie
print(Human.display_population())
alt_marie = Human.alternate_constructor({"name": "Marie"})
print(Human.display_population())
