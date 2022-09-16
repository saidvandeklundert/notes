import uuid
from datetime import datetime
from uuid import UUID

from fastapi import HTTPException
from starlette import status
from starlette.responses import Response

from web.app import app


from network.network_service.network import Device, Os, Vendor, Devices


devices: list[Device] = []
devices.append(Device(id=uuid.uuid4(), name="r1", os=Os.JUNOS, vendor=Vendor.JUNIPER))


@app.get("/devices", response_model=Devices)
def get_devices():
    """Returns all the Devices found in the database."""
    return {"devices": devices}


@app.post("/devices", status_code=status.HTTP_201_CREATED, response_model=Device)
def add_device(device: Device):
    """Add a Device to the database."""
    devices.append(device)
    return device


@app.put("/devices/{device_id}", response_model=Device)
def update_device(device_id: UUID, device_update: Device):
    """Update a Device in the database.

    All fields for the device need to be provided."""
    for idx, device in enumerate(devices):
        if device.id == device_id:
            update_data = device_update.dict(exclude_unset=True)
            updated_device = device.copy(update=update_data)
            devices[idx] = updated_device
            return device
    raise HTTPException(status_code=404, detail=f"Device with ID {device_id} not found")


"""
@app.delete(
    "/devices/{device_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    response_class=Response,
)
def delete_order(request: Request, device_id: UUID):
    try:
        with UnitOfWork() as unit_of_work:
            repo = OrdersRepository(unit_of_work.session)
            orders_service = OrdersService(repo)
            orders_service.delete_order(device_id=device_id, user_id=request.state.user_id)
            unit_of_work.commit()
        return
    except ValueError:
        raise HTTPException(
            status_code=404, detail=f"Device with ID {device_id} not found"
        )
"""
