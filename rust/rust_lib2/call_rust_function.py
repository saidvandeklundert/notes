import ctypes
from pydantic import BaseModel
from typing import List

rust = ctypes.CDLL("target/release/librust_lib2.so")


class ProcedureInput(BaseModel):
    timeout: int
    retries: int
    host_list: List[str]
    action: str
    job_id: int


class ProcedureOutput(BaseModel):
    job_id: int
    result: str
    message: str
    failed_hosts: List[str]


if __name__ == "__main__":
    procedure_input = ProcedureInput(
        timeout=10,
        retries=3,
        action="reboot",
        host_list=["server1", "server2"],
        job_id=1,
    )

    ptr = rust.start_procedure(procedure_input.json().encode("utf-8"))

    returned_bytes = ctypes.c_char_p(ptr).value

    procedure_output = ProcedureOutput.parse_raw(returned_bytes)
    print(procedure_output.json(indent=2))
