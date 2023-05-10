"""
In this case, we neglect the Single Responsibility Principle.

There is a class Human with a 'write_to_db' method.

The Human class stores attributes for a Human AND it stores things in a database.

The class will need to change:
- if the model of a Human changes
- if the database we use changes 


To adhere to the SRP, we should remove the 'write_to_db' method.
"""
from dataclasses import dataclass


@dataclass
class Human:
    name: str
    age: int
    stored_in_db: bool = False

    def write_to_db(self):
        print(f"Storing a record for {self.name} in the database.")
        self.stored_in_db = True


if __name__ == "__main__":
    jan = Human(name="Jan", age=6)
    print(vars(jan))
    jan.write_to_db()
    print(vars(jan))
