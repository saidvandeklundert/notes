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

    def install_os(self) -> None:
        print("Installing OS")

    def format_hd(self) -> None:
        print("Formatting the hard drive")

    def create_admin_user(self, password: str) -> None:
        print(f"Creating admin user with password {password}.")

    def factory_reset(self, password: str):
        self.format_hd()
        self.install_os()
        self.create_admin_user(password=password)


def main() -> None:
    laptop = Laptop()
    print(laptop)
    laptop.factory_reset("admin")


if __name__ == "__main__":
    main()
