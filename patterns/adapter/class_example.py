"""
Adapter intent:

to provide a unified interface that allows objects with incompatible
interfaces to collaborate.

"""


class Target:
    """The domain-specific inerface used by the client code."""

    def request(self) -> str:
        return "Target: the default behavior."


class Adaptee:
    """
    Class containing an incompatible interface with existing client code.

    This Adaptee needs adaptation before the client can use it.
    """

    def some_information(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target, Adaptee):
    """
    The Adapter makes the Adaptee's interface compatible with the Target's
    interface via multiple inheritance.
    """

    def request(self) -> str:
        return f"Adapter: (translated) {self.some_information()[::-1]}"


def client_code(target: "Target") -> None:
    """
    The client code supports all classes that follow the Target interface.
    """
    print(target.request(), end="")


if __name__ == "__main__":
    print("Client: I can work fine with the Target objects:")
    target = Target()

    client_code(target)

    print("\n")
    adaptee = Adaptee()

    print("The Adaptee has a strange interface:")
    print(adaptee.some_information())

    print("However, I can use the Adapter to translate it:")
    adapter = Adapter()
    client_code(adapter)
