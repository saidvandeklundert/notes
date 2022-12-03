from dataclasses import dataclass
import uuid
from enum import Enum


class TaskName(Enum):
    MIGRATE = "migrate"
    DELETE = "delete"


@dataclass
class Task:
    task_id: uuid.UUID
    task_name: TaskName
    message: str

    def dict(self):
        return {
            "task_id": str(self.task_id),
            "task_name": self.task_name.value,
            "message": self.message,
        }
