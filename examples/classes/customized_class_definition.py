"""
FLow control can be used inside classes. 

This offers flexibility as you can define methods differently based on a variety of things, for example:
- platform
- environment variables
- debug settings
- anything you can dream of

"""
import platform


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    if "win" in platform.system().lower():
        print("Initiliazing class on a Windows machine.")

        def method(self):
            print(f"{self.name} on windows!")

    else:

        def method(self):
            print(f"{self.name} on windows!")


jan = Human("jan", 6)
jan.method()