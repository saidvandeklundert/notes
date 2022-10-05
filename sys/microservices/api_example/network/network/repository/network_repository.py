from abc import ABC, abstractmethod
from uuid import UUID
import uuid
from network.network_service.network import Device, Os, Vendor, Devices
from network.network_service.exceptions import DeviceNotFoundError
from ezaws import DynamoDB, Region
import boto3
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


class InMemmoryCache(NetworkRepository):
    def __init__(self):
        self.devices: list[Device] = []
        self.devices.append(
            Device(
                id="ac591eeb-c963-435f-9e22-08242dbb53d6",
                name="r1",
                os=Os.JUNOS,
                vendor=Vendor.JUNIPER,
            )
        )
        self.devices.append(
            Device(
                id="ac591eeb-c963-435f-9e22-08242dbb53d7",
                name="r2",
                os=Os.IOSXR,
                vendor=Vendor.CISCO,
            )
        )

    def add(self, device: Device) -> Device:

        self.devices.append(device)
        return device

    def get(self, device_id: str) -> Device:
        for device in self.devices:
            if device.id == device_id:
                return device
        raise DeviceNotFoundError("Cannot find a device with ID {device_id}")

    def list(self, limit: None | int = None) -> list[Device]:
        return self.devices

    def update(self, device_id: str, device: Device) -> Device:
        for idx, existing_device in enumerate(self.devices):
            if existing_device.id == device_id:
                self.devices[idx] = device
                return device
        raise DeviceNotFoundError("Cannot find a device with ID {device_id}")

    def delete(self, device_id: str) -> Device:
        for idx, device in enumerate(self.devices):
            print(device.id, device_id)
            print(type(device.id), type(device_id))
            if device.id == device_id:
                del self.devices[idx]
                return

        raise DeviceNotFoundError("Cannot find a device with ID {device_id}")


class DynamoDBRepository(NetworkRepository):
    """
    >>> REPO = DynamoDBRepository(
            ddb_client=DynamoDB(region=Region.eu_central_1), table_name="Devices"
        )
    """

    def __init__(self, ddb_client: DynamoDB, table_name: str):
        self.ddb_client = ddb_client
        self.table_name = table_name

    def add(self, device: Device) -> Device:

        self.ddb_client.put_item(table_name=self.table_name, item=device.dict())
        return device

    def get(self, device_id: str) -> Device:
        """
        ={'server': 'Server', 'date': 'Mon, 19 Sep 2022 18:11:40 GMT', 'content-type': 'application/x-amz-json-1.0', 'content-length': '2', 'connection': 'keep-alive', 'x-amzn-requestid': '2F1AH1CHVTA1CG2JU0R15AK00RVV4KQNSO5AEMVJF66Q9ASUAAJG', 'x-amz-crc32': '2745614147'}, RetryAttempts=0))
        GetItemResponse(Item={'id': 'ac591eeb-c963-435f-9e22-08242dbb53d6', 'name': 'r1', 'os': 'junos', 'vendor': 'juniper'}, ResponseMetadata=ResponseMetadata(RequestId='I2I09GMIQS2KSP38GE459UVQURVV4KQNSO5AEMVJF66Q9ASUAAJG', HostId=None, HTTPStatusCode=200, HTTPHeaders={'server': 'Server', 'date': 'Mon, 19 Sep 2022 18:11:40 GMT', 'content-type':
        'application/x-amz-json-1.0', 'content-length': '122', 'connection': 'keep-alive', 'x-amzn-requestid': 'I2I09GMIQS2KSP38GE459UVQURVV4KQNSO5AEMVJF66Q9ASUAAJG', 'x-amz-crc32': '2964509650'}, RetryAttempts=0))
        """
        result = self.ddb_client.get_item(
            table_name=self.table_name, item={"id": device_id}
        )
        if result.Item:
            return Device(**result.Item)
        raise DeviceNotFoundError("Cannot find a device with ID {device_id}")

    def list(self, limit: None | int = None) -> list[Device]:
        result = self.ddb_client.scan(table_name=self.table_name)

        deserializer = boto3.dynamodb.types.TypeDeserializer()

        def deserialize(d: dict):
            return {k: deserializer.deserialize(v) for k, v in d.items()}

        python_data = [deserialize(d) for d in result.Items]
        devices = [Device(**d) for d in python_data]

        return devices

    def update(self, device_id: str, device: Device) -> Device:

        result = self.ddb_client.get_item(
            table_name=self.table_name, item={"id": str(device_id)}
        )
        if result.Item:
            self.ddb_client.put_item(table_name=self.table_name, item=device.dict())
            return device

        raise DeviceNotFoundError("Cannot find a device with ID {device_id}")

    def delete(self, device_id: str) -> Device:
        device = self.get(device_id=device_id)

        self.ddb_client.delete_item(
            table_name=self.table_name, item={"id": str(device.id)}
        )
        return device


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
        raise DeviceNotFoundError("Cannot find a device with ID {device_id}")

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

    def delete(self, device_id: str) -> Device:

        query = f"DELETE from Devices where id = '{device_id}';"
        connection = sqlite3.connect("test_db")
        connection.execute(query)
        connection.commit()

        return


if __name__ == "__main__":
    REPO = SqlLiteRepo()
