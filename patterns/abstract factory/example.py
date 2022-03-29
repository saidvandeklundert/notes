"""
The intent of the abstract factory design pattern is to let you
 produce families of related objects without specifying their concrete classes.
"""
from abc import ABC, abstractmethod

"""
Product families should have their own base interface:
"""


class AbstractProductA(ABC):
    @abstractmethod
    def concrete_specific(self) -> str:
        pass


class AbstractProductB(ABC):
    @abstractmethod
    def concrete_b_specific(self) -> str:
        pass


"""
The concrete Products should be created by corresponding Concrete Factories:
"""


class ConcreteProductA1(AbstractProductA):
    def concrete_specific(self) -> str:
        return "ConcreteProductA1"


class ConcreteProductA2(AbstractProductA):
    def concrete_specific(self) -> str:
        return "ConcreteProductA1"


class ConcreteProductB1(AbstractProductB):
    def concrete_b_specific(self) -> str:
        return "B1"


class ConcreteProductB2(AbstractProductB):
    def concrete_b_specific(self) -> str:
        return "B2"


"""
There should be an abstract factory defined,
 this gives the interface that other factories should satisfy:
"""


class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


"""
Concrete factories produce a family of products that belong to a single
variant.

Through the specification of the base interface, the concrete factories are
able to guarantee that the resulting products are compatible.

Signatures of the concrete factory's methods return an abstract product,
 while INSIDE the method a concrete product is instantiated.
"""


class ConcreteFactory1(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()


def client_code(factory: AbstractFactory) -> None:
    """
    The client works with factories and products only through abstract types:
    - AbstractFactory
    - AbstractProduct

    This lets you pass any factory or product subclass to the client code
     without breaking it.
    """
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(product_a.concrete_specific())
    print(product_b.concrete_b_specific())


if __name__ == "__main__":
    client_code(ConcreteFactory1())
    client_code(ConcreteFactory2())
