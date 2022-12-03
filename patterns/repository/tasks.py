from repository_model import Task, TaskName
import uuid

tasks: list[Task] = []


tasks.append(
    Task(
        task_id=uuid.uuid4(),
        task_name=TaskName.DELETE,
        message="remove sidestore",
    ),
)
tasks.append(
    Task(
        task_id=uuid.uuid4(),
        task_name=TaskName.DELETE,
        message="remove sidestore",
    ),
)
tasks.append(
    Task(
        task_id="e11f0d65-a502-42e5-b373-23d84ce2c244",
        task_name=TaskName.MIGRATE,
        message="up side down",
    ),
)

existing_task = Task(
    task_id="e11f0d65-a502-42e5-b373-23d84ce2c244",
    task_name=TaskName.MIGRATE,
    message="up side down",
)
