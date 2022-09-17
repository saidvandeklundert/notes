from abc import ABC, abstractmethod
from uuid import UUID
import uuid
from network.network_service.network import Device, Os, Vendor, Devices
from network.network_service.exceptions import DeviceNotFoundError


class NetworkRepository(ABC):
    @abstractmethod
    def add(self, device: Device) -> Device:
        pass

    @abstractmethod
    def get(self, device_id: UUID) -> Device:
        pass

    @abstractmethod
    def list(self, limit: None | int = None) -> list[Device]:
        pass

    @abstractmethod
    def update(self, device_id: UUID, device: Device) -> Device:
        pass

    @abstractmethod
    def delete(self, device_id: UUID) -> Device:
        pass


class InMemmoryCache(NetworkRepository):
    def __init__(self):
        self.devices: list[Device] = []
        self.devices.append(
            Device(id=uuid.uuid4(), name="r1", os=Os.JUNOS, vendor=Vendor.JUNIPER)
        )
        self.devices.append(
            Device(id=uuid.uuid4(), name="r2", os=Os.IOSXR, vendor=Vendor.CISCO)
        )

    def add(self, device: Device) -> Device:

        self.devices.append(device)
        return device

    def get(self, device_id: UUID) -> Device:
        for device in self.devices:
            if device.id == device_id:
                return device
        raise DeviceNotFoundError("Cannot find a device with ID {device_id}")

    def list(self, limit: None | int = None) -> list[Device]:
        return self.devices

    def update(self, device_id: UUID, device: Device) -> Device:
        for idx, device in enumerate(self.devices):
            if device.id == device_id:
                self.devices[idx] = device
                return device
        raise DeviceNotFoundError("Cannot find a device with ID {device_id}")

    def delete(self, device_id: UUID) -> Device:
        for idx, device in enumerate(self.devices):
            if device.id == device_id:
                del self.devices[idx]
                return

        raise DeviceNotFoundError("Cannot find a device with ID {device_id}")
