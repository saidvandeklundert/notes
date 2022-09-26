from network.network_service.exceptions import DeviceNotFoundError
from network.repository.network_repository import NetworkRepository
from uuid import UUID
import uuid
from network.network_service.network import Device, Os, Vendor, Devices


class NetworkService:
    def __init__(self, network_repo: NetworkRepository):
        self.network_repo = network_repo

    def add_device(self, device: Device) -> Device:
        return self.network_repo.add(device)

    def list_devices(self) -> list[Device]:
        return self.network_repo.list()

    def update_device(self, device_id: str, device: Device) -> Device:
        return self.network_repo.update(device_id, device)

    def delete_device(self, device_id: str) -> Device:
        print("delete", device_id)
        return self.network_repo.delete(device_id)
