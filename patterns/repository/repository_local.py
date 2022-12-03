from repository_model import Task
from repository import Repository
from repository_exeption import RepositoryExeption
from tasks import tasks, existing_task
import uuid
import json


class LocalRepository(Repository):
    def __init__(self, repo_location: str = "repository.json"):
        self.repo_location = repo_location
        self._initialize_repo()

    def _initialize_repo(self) -> None:
        """Check if we can open an existing repo.

        Create one if we cannot."""
        try:
            with open(self.repo_location, "r") as f:
                _ = json.load(f)
        except json.JSONDecodeError:
            with open(self.repo_location, "w") as f:
                json.dump({}, f)

    def create(self, task: Task) -> None:
        with open(self.repo_location, "r") as f:
            repository = json.load(f)
        task_id = str(task.task_id)
        if repository.get(task_id) is None:
            repository[str(task.task_id)] = task.dict()
            with open(self.repo_location, "w") as f:
                json.dump(repository, f)

        else:
            raise RepositoryExeption(
                f"Record for {task_id} already exists, use update."
            )

    def read(self, task_id: uuid.UUID) -> Task:
        with open(self.repo_location, "r") as f:
            repository = json.load(f)
        task_id_str = str(task_id)
        if repository.get(task_id_str) is None:
            raise RepositoryExeption(f"Record for {task_id} does not exist.")
        else:
            return Task(**repository[task_id])

    def update(self, task: Task) -> None:
        with open(self.repo_location, "r") as f:
            repository = json.load(f)
        task_id = str(task.task_id)
        if repository.get(task_id):
            repository[str(task.task_id)] = task.dict()
            with open(self.repo_location, "w") as f:
                json.dump(repository, f)
        else:
            raise RepositoryExeption(
                f"Record for {task_id} does not exist, use create."
            )

    def delete(self, task: Task) -> None:
        with open(self.repo_location, "r") as f:
            repository = json.load(f)
        task_id = str(task.task_id)
        del repository[task_id]
        with open(self.repo_location, "w") as f:
            json.dump(repository, f)

    def load(self) -> list[Task]:
        with open(self.repo_location, "r") as f:
            repository = json.load(f)

        task_list = []

        for v in repository.values():
            task_list.append(Task(**v))

        return task_list


if __name__ == "__main__":
    local_repo = LocalRepository(repo_location="repository.json")

    for task in tasks:
        local_repo.create(task=task)
        print(f"created task {task.task_id}")

    print(local_repo.read(existing_task.task_id))
    print(local_repo.load())
