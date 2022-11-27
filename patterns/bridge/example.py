"""
Bridge Design Pattern

Intent: Lets you split a large class or a set of closely related classes into
two separate hierarchies—abstraction and implementation—which can be developed
independently of each other.

              A
           /     \                        A         N
         Aa      Ab        ===>        /     \     / \
        / \     /  \                 Aa(N) Ab(N)  1   2
      Aa1 Aa2  Ab1 Ab2



            Exchanges abstraction <-  bridge -> Tradingbot abstraction
    Binance                                         AggroBot
    Coinbase                                        SafeBot
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Abstraction:
    """
    The abstraction defines the interface for the "control" part.

    It maintains a reference to an object of the Implementation hierarchy
    and delegates all real work to this object.
    """

    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation

    def operation(self) -> str:
        return (
            f"Abstraction: Base operation with:\n"
            f"{self.implementation.operation_implementation()}"
        )


class ExtendedAbstraction(Abstraction):
    """
    You can extend the Abstraction without changing the Implementation class.
    """

    def operation(self) -> str:
        return (
            f"ExtendedAbstraction: Extended operation with:\n"
            f"{self.implementation.operation_implementation()}"
        )


class Implementation(ABC):
    """
    The implementation defines the interface for all implementation classes.

    It does not have to match the Abstraction's interface. In fact, the two
    interfaces can be entirely different.
    Typically, the Implementation interface provides only primitive operations,
    while the Abstraction defines higher-level operations based on those primitives.
    """

    @abstractmethod
    def operation_implementation(self) -> str:
        pass


"""
Each concrete Implementation corresponds to a specific platform and implements
the Implementation interface using that platform's API.
"""


class ConcreteImplementationA(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationA: Here is the result on Platform A."


class ConcreteImplementationB(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationB: Here is the result on Platform B."


def client_code(abstraction: Abstraction) -> None:
    """
    Except or the initialization phase, where an Abstraction object gets linked
    without specific Implementation object, the client code should only
    depend on the Abstraction class. This way the client code can support
    any abstraction-implementation combination.
    """
    print(abstraction.operation())


if __name__ == "__main__":
    """
    The client code should be able to work with any pre-configured abstraction-
    implementation combination.
    """

    implementation = ConcreteImplementationA()
    abstraction = Abstraction(implementation)
    client_code(abstraction)

    print("\n")

    implementation = ConcreteImplementationB()
    abstraction = ExtendedAbstraction(implementation)
    client_code(abstraction)
