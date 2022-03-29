from abc import ABC, abstractmethod


class ShapeFactory(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Rectangle(ShapeFactory):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_area(self):
        return self.height * self.width

    def calculate_perimeter(self):
        return 2 * (self.height * self.width)


class Circle(ShapeFactory):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius


class Square(ShapeFactory):
    def __init__(self, width):
        self.width = width

    def calculate_area(self):
        return self.width**2

    def calculate_perimeter(self):
        return 4 * self.width


class ReadShapeFactory:
    def create_shape(self, kwargs):
        if kwargs["name"] == "circle":
            return Circle(float(kwargs["radius"]))

        elif kwargs["name"] == "rectangle":
            return Rectangle(kwargs["height"], kwargs["width"])

        elif kwargs["name"] == "square":
            return Square(kwargs["width"])


if __name__ == "__main__":
    read_factory = ReadShapeFactory()
    circle = read_factory.create_shape({"name": "circle", "radius": 3.4})
    print(circle.calculate_area())
    square = read_factory.create_shape({"name": "square", "width": 8})
    print(square.calculate_area())

    rectangle = read_factory.create_shape(
        {"name": "rectangle", "height": 8, "width": 20}
    )
    print(rectangle.calculate_area())
