"""
Like traits in Rust, abstract base classes can be used to enfore a 'something' to adhere to a contract.

In the case of python, this something is a class and the contract is the implementation of methods.

Example is in case you want to create messengers that all adhere to being able to relay a message:
"""
from abc import ABC, abstractmethod


class Messenger(ABC):
    """inheriting this ABC will enfore the class to implement 2 methods."""

    @abstractmethod
    def message(self):
        pass

    @abstractmethod
    def priority_message(self):
        pass


class HorseRiderMessenger(Messenger):
    def __init__(self, letter: str):
        self.letter = letter

    def message(self):
        return self.letter

    def priority_message(self):
        return self.letter


horse_rider_message = HorseRiderMessenger("some_important_news")


class MailManMessenger(Messenger):
    """This class will not work because it does not adhere to the contract.

    It does not implement all required methods.
    `"""

    def __init__(self, letter: str):
        self.letter = letter

    def message(self):
        return self.letter


try:
    some_dude = MailManMessenger("important message")
    print(some_dude.message())
except Exception as err:
    print(err)