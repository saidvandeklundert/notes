from tempfile import NamedTemporaryFile
import shutil
import csv
import uuid

filename = "network.csv"
tempfile = NamedTemporaryFile(mode="w", delete=False, newline="")

fields = [
    "hostname",
    "serial",
    "vendor",
    "product",
    "os",
    "version",
    "life_cycle",
    "status",
]


def return_row_map(hostname, serial, vendor, product, os, version, life_cycle, status):
    return {
        "hostname": hostname,
        "serial": serial,
        "vendor": vendor,
        "product": product,
        "os": os,
        "version": version,
        "life_cycle": life_cycle,
        "status": status,
    }


with open(filename, "r", newline="", encoding="utf-8") as csvfile, tempfile:
    reader = csv.DictReader(csvfile, fieldnames=fields)
    writer = csv.DictWriter(tempfile, fieldnames=fields)
    for row_map in reader:
        print(row_map)
        row_map["serial"] = str(uuid.uuid4()).upper()[:8]
        writer.writerow(row_map)

shutil.move(tempfile.name, filename)
