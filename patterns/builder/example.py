"""
The Builder pattern.

Allows the step by step construction of complext objects. 

The patterns allows you to produce different types and representations of an 
object using the same construction code.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Builder(ABC):
    """
    The Builder itself is an interface that specifies methods for creating
    the different parts of the Product objects.
    """

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_part_a(self) -> None:
        pass

    @abstractmethod
    def produce_part_b(self) -> None:
        pass

    @abstractmethod
    def produce_part_c(self) -> None:
        pass


class ConcreteBuilder1(Builder):
    """

    The ConcreteBuilder classes follow the builder interface and provide
    specific implementations of the building steps.

    Your program may have several variations of Builders, implemented differently."""

    def __init__(self) -> None:
        """A new builder instance should contain a black product object."""
        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    @property
    def product(self) -> Product1:
        """
        Concrete Builders provide their own methods for retrieving results.
        The reson for this is that various Builders may create
        different products that do not follow the same interface.

        Therefore, such methods cannot be declared in the base Builder interface.

        Usualy, after returnng the end result to the client, a builder
        instance is expected to be ready to start producing another product

        That is why it is a usual practice to call the reset method of the end of the getproduct
        method body. However, this behavior is not mandatory, and you
        can make your builders wait for an explicit reset call from
        the client code before disposing of the previous result.
        """

        product = self._product
        self.reset()
        return product

    def produce_part_a(self) -> None:
        self._product.add("PartA")

    def produce_part_b(self) -> None:
        self._product.add("PartB1")

    def produce_part_c(self) -> None:
        self._product.add("PartC1")


class Product1:
    """
    The Builder pattern only makes sense in case your products are quite complex.

    Unlike other creational patterns, different concrete builders can produce
    unrelated products. In other words, results of various builders may not
    always follow the same interface.
    """

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")


class Director:
    """The director is only responsible for executing the building steps in
    a particular sequence. It is helpful when producing products according to
    a specific order or configuration. Strictly speaking, the Director class
    is optional, since the client can control the builders directly."""

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        """
        The Director works with any Builder instance that the client code
        passes into it. This way, the client code may alter the final type of
        the newly assembled product.
        """
        self._builder = builder

    """
    The Director can construct several product variations using the same building
    steps.
    """

    def build_minimal_viable_product(self) -> None:
        self.builder.produce_part_a()

    def build_full_featured_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()


if __name__ == "__main__":
    """
    The client code creates the builder object, passes it to the directory and
    then initiats the construction process.

    The end result is retrieved from the builder object.
    """

    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    print("Standard product:")
    director.build_minimal_viable_product()
    builder.product.list_parts()

    print("\n")

    print("Standard full featured product: ")
    director.build_full_featured_product()
    builder.product.list_parts()

    print("\n")

    # Remember, the Builder pattern can be used without a Director class.
    print("Custom product: ")
    builder.produce_part_a()
    builder.produce_part_b()
    builder.product.list_parts()
