import sqlite3
from network.network_service.network import Device


if __name__ == "__main__":
    conn = sqlite3.connect("test_db")

    conn.execute(
        """CREATE TABLE Devices
            (id INT PRIMARY KEY     NOT NULL,
            name           TEXT    NOT NULL,
            os            TEXT     NOT NULL,
            vendor            TEXT     NOT NULL);"""
    )

    conn.commit()
    query = "INSERT INTO Devices (id,name,os,vendor) VALUES ('ac591eeb-c963-435f-9e22-08242dbb54d6', 'R20', 'junos', 'juniper' )"
    conn.execute(query)
    conn.commit()
    cursor = conn.execute("SELECT id, name, os,vendor from Devices")

    for row in cursor:
        print(f"id: {row[0]} name: {row[1]} os: {row[2]} vendor: {row[3]} ")
        device = Device(
            **{"id": row[0], "name": row[1], "os": row[2], "vendor": row[3]}
        )
        print(device.json())

    cursor = conn.execute(
        "SELECT id, name, os,vendor from Devices where id = 'ac591eeb-c963-435f-9e22-08242dbb54d6'"
    )
    for row in cursor:
        print(f"RESULT: id: {row[0]} name: {row[1]} os: {row[2]} vendor: {row[3]} ")

    conn.close()
