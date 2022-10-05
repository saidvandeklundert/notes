from dataclasses import dataclass
import requests
from network.network_service.network import Device, Devices


@dataclass
class ExampleClient:
    base_url: str
    port: str

    def get_devices(self) -> Devices:
        response = requests.get(f"{self.base_url}:{self.port}/devices")

        devices = Devices(**response)
        return devices


if __name__ == "__main__":

    client = ExampleClient(base_url="http://127.0.0.1", port="8000")
    print(client.get_devices())
