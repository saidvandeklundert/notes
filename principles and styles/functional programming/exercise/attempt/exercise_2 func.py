"""
We want to add the capability to the software to reset the laptop to the factory settings. 
This involves the following steps:

    Format the hard drive.
    Make sure the machine name is set to "DULL", which is the name of the company that produced the laptop.
    Install the os.
    Create an admin user with password "admin"

a) Extend the program with this capability relying on object-oriented programming.

b) Write another version of the same program, 
    but this time, don't extend the class with new capabilities, 
    use a separate function instead. 
    
    How would you describe the differences between the two versions?

"""
from dataclasses import dataclass


@dataclass
class Laptop:
    machine_name: str = "DULL"


def format_hd(laptop):
    print("Formatting the hard drive")
    return laptop


def install_os(laptop) -> Laptop:
    print("Installing OS")
    return laptop


def create_admin_user(laptop: Laptop, password: str) -> Laptop:
    print("create user")


def factory_reset(laptop: Laptop) -> Laptop:
    format_hd(laptop)
    install_os(laptop)
    create_admin_user(laptop, "admin")
    return laptop


def main() -> None:
    laptop = Laptop()
    print(laptop)
    laptop = factory_reset(laptop=laptop)


if __name__ == "__main__":
    main()
