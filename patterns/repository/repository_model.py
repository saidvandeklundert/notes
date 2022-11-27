from dataclasses import dataclass
import uuid
from enum import Enum


class TaskResult(Enum):
    SUCCESS = "success"
    FAILED = "failed"
    CANCELLED = "cancelled"
    NOT_STARTED = "not started"
    INCOMPLETE = "incomplete"


class TaskName(Enum):
    MIGRATE = "migrate"
    DELETE = "delete"


class TaskStatus(Enum):
    NEW = "new"
    IN_PROGRESS = "in progress"
    COMPLETED = "completed"


@dataclass
class Task:
    task_id: uuid.UUID
    result: TaskResult
    task_name: TaskName
    task_status: TaskStatus
    message: str
