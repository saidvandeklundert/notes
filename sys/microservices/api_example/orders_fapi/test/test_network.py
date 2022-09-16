from fastapi import FastAPI
from fastapi.testclient import TestClient
from network.network_service.network import Devices
from web.app import app


client = TestClient(app)


def test_read_main():
    response = client.get("/devices")
    assert response.status_code == 200
    # test if we can turn response into Devices
    assert isinstance(Devices(**response.json()), Devices)
