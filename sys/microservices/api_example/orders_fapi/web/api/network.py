import uuid
from datetime import datetime
from uuid import UUID

from fastapi import HTTPException
from starlette import status
from starlette.responses import Response

from web.app import app


from network.network_service.network import Device, Os, Vendor, Devices
from network.network_service.exceptions import DeviceNotFoundError
from network.network_service.network_service import NetworkService
from network.repository.network_repository import InMemmoryCache

devices: list[Device] = []
devices.append(Device(id=uuid.uuid4(), name="r1", os=Os.JUNOS, vendor=Vendor.JUNIPER))

REPO = InMemmoryCache()


@app.get("/devices", response_model=Devices)
def get_devices():
    """Returns all the Devices found in the database."""
    network_service = NetworkService(REPO)
    return {"devices": network_service.list_devices()}


@app.post("/devices", status_code=status.HTTP_201_CREATED, response_model=Device)
def add_device(device: Device):
    """Add a Device to the database."""

    network_service = NetworkService(REPO)
    network_service.add_device(device=device)
    return device


@app.put("/devices/{device_id}", response_model=Device)
def update_device(device_id: UUID, device_update: Device):
    """Update a Device in the database.

    All fields for the device need to be provided."""
    network_service = NetworkService(REPO)
    try:
        network_service.delete_device(device_id=device_id)
    except DeviceNotFoundError:
        raise HTTPException(
            status_code=404, detail=f"Device with ID {device_id} not found"
        )


@app.delete(
    "/devices/{device_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    response_class=Response,
)
def delete_order(device_id: UUID):
    network_service = NetworkService(REPO)
    try:
        network_service.delete_device(device_id=device_id)
    except DeviceNotFoundError:
        raise HTTPException(
            status_code=404, detail=f"Device with ID {device_id} not found"
        )
