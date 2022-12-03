from typing import List


class ActiveWorker:
    def __init__(self, name: str, age: int, city: str):
        self.name = name
        self.age = age
        self.city = city
        self._rucksack: List[str] = list()

    def report_for_duty(self) -> str:
        return f"worker {self.name} reporting for duty!"

    def carry_item(self, item: str) -> None:
        self._rucksack.append(item)

    def carry_items(self, items: List[str]) -> None:
        self._rucksack.extend(items)

    def unload_items(self) -> List[str]:
        to_unload = self._rucksack.copy()
        self._rucksack = list()
        return to_unload
