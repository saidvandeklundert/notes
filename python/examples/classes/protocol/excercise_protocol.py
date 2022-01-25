from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Protocol


class Pricing(Protocol):
    def get_total_price(self) -> int:
        ...


@dataclass
class PricePerDay:
    price_per_day: int
    nr_days: int

    def get_total_price(self):
        return int(self.price_per_day * self.nr_days)


@dataclass
class PricePerMonth:
    price_per_month: int
    nr_months: int

    def get_total_price(self):
        return int(self.price_per_month * self.nr_months)


@dataclass
class PricePerKm:
    price_per_km: int
    nr_kms: int

    def get_total_price(self):
        return int(self.price_per_km * self.nr_kms)


class FuelType(Enum):
    PETROL = auto()
    DIESEL = auto()
    ELECTRIC = auto()


class TruckCabStyle(Enum):
    REGULAR = auto()
    EXTENDED = auto()
    CREW = auto()


@dataclass
class Vehicle:
    brand: str
    model: str
    color: str
    fuel_type: FuelType
    license_plate: str
    reserved: bool
    pricing: list[Pricing] = field(default_factory=list)


@dataclass
class CarPerDay(Vehicle):
    number_of_seats: int = 5
    storage_capacity_litres: int = 40


@dataclass
class Truck(Vehicle):
    cab_style: TruckCabStyle = TruckCabStyle.REGULAR


@dataclass
class Trailer:
    brand: str
    model: str
    capacity_m3: int
    price_per_month: int
    reserved: bool


def main():
    pass


if __name__ == "__main__":
    main()
