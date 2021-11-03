import ctypes
from pydantic import BaseModel
from typing import List
import random

rust = ctypes.CDLL("target/release/librust_lib2.so")


class PythonModel(BaseModel):
    timeout: int
    retries: int
    host_list: List[str]
    action: str
    job_id: int


class RustResult(BaseModel):
    job_id: int
    result: str
    message: str
    failed_hosts: List[str]


if __name__ == "__main__":

    i = 10000

    while i > 0:
        random_number = random.randint(10000, 20000)
        hosts = [f"server-{x}" for x in range(1, random_number)]
        model = PythonModel(
            timeout=10,
            retries=3,
            action="reboot",
            host_list=hosts,
            job_id=i,
        )

        ptr = rust.start_procedure(model.json().encode("utf-8"))

        returned_bytes = ctypes.c_char_p(ptr).value

        returned_model = RustResult.parse_raw(returned_bytes)
        print(returned_model)
