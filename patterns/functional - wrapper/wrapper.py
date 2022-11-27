"""
The wrapper pattern is when one function is wrapped around another function, providing
 some means to controll the inner function.

In this example, there is a discount function. This discount function is wrapped by
 the loyalty program, which controls the discount based on some customer loyalty.

"""
from enum import Enum


class Loyalty(Enum):
    BRONZE = 5
    SILVER = 10
    GOLD = 20


def calculate_price(price: int, discount: int) -> int:
    """function that will be wrapped."""
    discount = int(price * (discount / 100))
    return price - discount


def localty_program_price(price: int, loyalty: Loyalty):
    """Function that will wrap calculate_price."""
    discount = {Loyalty.BRONZE: 5, Loyalty.SILVER: 10, Loyalty.GOLD: 20}
    return calculate_price(price=price, discount=discount[loyalty])


def main() -> None:
    loyalty_1 = Loyalty.BRONZE
    loyalty_2 = Loyalty.GOLD
    price = 100
    print(localty_program_price(price=price, loyalty=loyalty_1))
    print(localty_program_price(price=price, loyalty=loyalty_2))


if __name__ == "__main__":
    main()
