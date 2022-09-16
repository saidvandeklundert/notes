from typing import Protocol
from typing import Any, List

DataObject = dict[str, Any]


class DataInterface(Protocol):
    def read_by_id(self, id: int) -> DataObject:
        ...

    def read_all() -> List[DataObject]:
        ...

    def create(self, data: DataObject) -> DataObject:
        ...

    def update(self, id: int, data: DataObject) -> DataObject:
        ...

    def delete(self, id: int, data: DataObject) -> DataObject:
        ...
