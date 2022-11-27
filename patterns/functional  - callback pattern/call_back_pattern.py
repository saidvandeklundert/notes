"""
In the callback pattern, we pass a function as an argument.

In this example, our app produces a JobResult.

The JobReslt can take a number of job handlers, which are functions
 that operate on the JobResult.

After the JobResult is instatiated, the port init runs all the functions 
 that have been passed in as a list called 'job_handlers'.
"""
from __future__ import annotations
from typing import Callable
from dataclasses import dataclass, field


@dataclass
class JobResult:
    result: bool
    data: str
    job_id: int
    job_handlers: list[JobHandler] = field(default_factory=list)

    def complete(self):
        for jobhandler in self.job_handlers:
            jobhandler(self)

    def __post_init__(self):
        for jobhandler in self.job_handlers:
            jobhandler(self)


JobHandler = Callable[[JobResult], None]


def log_to_disk(jr: JobResult) -> None:
    print(f"logging JobResult to disk: id {jr.job_id} data: {jr.data}")


def store_in_ddb(jr: JobResult) -> None:
    print(f"store job {jr.job_id} in DynamoDB")


def clean_logs(jr: JobResult) -> None:
    print(f"cleaning up the logs for {jr.job_id}")


def success_dashboard_update(jr: JobResult) -> None:
    print(f"{jr.job_id} was a success, updating the dashboard.")


def main() -> None:
    job_handlers = [log_to_disk, store_in_ddb, clean_logs, success_dashboard_update]
    JobResult(result=False, data="did not go well", job_id=1, job_handlers=job_handlers)

    JobResult(result=True, data="went as planned", job_id=2, job_handlers=job_handlers)


if __name__ == "__main__":
    main()
