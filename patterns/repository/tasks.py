from repository_model import Task, TaskResult, TaskName, TaskStatus
import uuid

tasks: list[Task] = []


tasks.append(
    Task(
        task_id=uuid.uuid4(),
        result=TaskResult.NOT_STARTED,
        task_name=TaskName.DELETE,
        task_status=TaskStatus.NEW,
        message="remove sidestore",
    ),
)
tasks.append(
    Task(
        task_id=uuid.uuid4(),
        result=TaskResult.SUCCESS,
        task_name=TaskName.DELETE,
        task_status=TaskStatus.COMPLETED,
        message="remove sidestore",
    ),
)
tasks.append(
    Task(
        task_id=uuid.uuid4(),
        result=TaskResult.INCOMPLETE,
        task_name=TaskName.MIGRATE,
        task_status=TaskStatus.IN_PROGRESS,
        message="up side down",
    ),
)
