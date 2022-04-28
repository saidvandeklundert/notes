"""
Builder according to "Effective Java", by Joshua Bloch. 

"Consider a builder when faced with many constructor parameters."

https://stackoverflow.com/questions/757743/what-is-the-difference-between-builder-design-pattern-and-factory-design-pattern

"""


from dataclasses import dataclass


@dataclass
class Fruit:
    name: str
    color: str
    firmness: str


class FruitBuilder:
    def __init__(self):
        self.name = None
        self.color = None
        self.firmness = None

    def set_name(self, name):
        self.name = name

    def set_color(self, color):
        self.color = color

    def set_firmness(self, firmness):
        self.firmness = firmness

    def build(self):
        return Fruit(name=self.name, color=self.color, firmness=self.firmness)


builder = FruitBuilder()
builder.set_color("red")
builder.set_name("apple")
builder.set_firmness("super_firm")
apple = builder.build()
print(apple)
