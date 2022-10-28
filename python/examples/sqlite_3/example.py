from abc import ABC, abstractmethod
from uuid import UUID
import uuid
from models import Device, Os, Vendor, Devices

import sqlite3


class NetworkRepository(ABC):
    @abstractmethod
    def add(self, device: Device) -> Device:
        pass

    @abstractmethod
    def get(self, device_id: str) -> Device:
        pass

    @abstractmethod
    def list(self, limit: None | int = None) -> list[Device]:
        pass

    @abstractmethod
    def update(self, device_id: str, device: Device) -> Device:
        pass

    @abstractmethod
    def delete(self, device_id: str) -> None:
        pass


class SqlLiteRepo(NetworkRepository):
    def __init__(self):
        self.db_name: str = "test_db"

    def add(self, device: Device) -> Device:

        query = f"INSERT INTO Devices (id,name,os,vendor) VALUES ('{device.id}', '{device.name}', '{device.os}', '{device.vendor}' )"
        connection = sqlite3.connect("test_db")
        connection.execute(query)
        connection.commit()

        return device

    def get(self, device_id: str) -> Device:
        connection = sqlite3.connect("test_db")
        cursor = connection.execute(
            f"SELECT id, name, os,vendor from Devices where id = '{device_id}'"
        )
        devices = []
        for row in cursor:

            devices.append(
                Device(**{"id": row[0], "name": row[1], "os": row[2], "vendor": row[3]})
            )
        if len(devices) == 1:
            return devices[0]
        raise ValueError("Cannot find a device with ID {device_id}")

    def list(self, limit: None | int = None) -> list[Device]:
        connection = sqlite3.connect(self.db_name)
        cursor = connection.execute(f"SELECT id, name, os,vendor from Devices")
        devices = []
        for row in cursor:

            devices.append(
                Device(**{"id": row[0], "name": row[1], "os": row[2], "vendor": row[3]})
            )

        return devices

    def update(self, device_id: str, device: Device) -> Device:
        raise NotImplemented()

    def delete(self, device_id: str) -> None:

        query = f"DELETE from Devices where id = '{device_id}';"
        connection = sqlite3.connect("test_db")
        connection.execute(query)
        connection.commit()

        return


if __name__ == "__main__":
    devices = [
        Device(
            id="ac591eeb-c963-435f-9e22-08242dbb53d6",
            name="r1",
            os=Os.JUNOS,
            vendor=Vendor.JUNIPER,
        ),
        Device(
            id="ac591eeb-c963-435f-9e22-08242dbb53d7",
            name="r2",
            os=Os.IOSXR,
            vendor=Vendor.CISCO,
        ),
    ]
    REPO = SqlLiteRepo()
    for device in devices:
        REPO.add(device)
    result = REPO.list()
    print(result)
