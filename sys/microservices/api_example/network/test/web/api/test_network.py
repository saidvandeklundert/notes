"""
python -m pytest .\test\
"""
from fastapi.testclient import TestClient
from network.network_service.network import Devices, Device
from web.app import app


client = TestClient(app)


def test_get_devices():
    response = client.get("/devices")
    assert response.status_code == 200
    # test if we can turn response into Devices
    assert isinstance(Devices(**response.json()), Devices)


def test_add_device():
    json_value = {
        "id": "ba7d2a92-8db6-4750-a183-18ed766c296f",
        "name": "string",
        "os": "ios",
        "vendor": "juniper",
    }
    response = client.post("/devices", json=json_value)

    assert response.status_code == 201
    # test if we can turn response into Devices
    assert isinstance(Device(**response.json()), Device)


def test_delete_device():
    response = client.delete("/devices/ac591eeb-c963-435f-9e22-08242dbb53d6")
    # 204 (No Content)
    # indicates that the server has fulfilled the request and that there
    # is no content to send in the response payload body.
    assert response.status_code == 204
