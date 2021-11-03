import ctypes
from pydantic import BaseModel
from typing import List

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
    model = PythonModel(
        timeout=10, retries=3, action="reboot", host_list=["server1", "server2"]
    )
    some_bytes = model.json().encode("utf-8")

    ptr = rust.start_procedure(some_bytes)

    returned_bytes = ctypes.c_char_p(ptr).value

    if returned_bytes:
        returned_model = RustResult.parse_raw(returned_bytes)
        print(returned_model.json(indent=2))
