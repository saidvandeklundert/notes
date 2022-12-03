from repository_model import Task
from repository import Repository
from repository_exeption import RepositoryExeption
from tasks import tasks, existing_task
import uuid
import sqlite3


def setup_db():
    conn = sqlite3.connect("repo_db")

    conn.execute(
        """CREATE TABLE Tasks
            (task_id INT PRIMARY KEY    NOT NULL,
            task_name           TEXT    NOT NULL,
            message        TEXT    NOT NULL);"""
    )

    conn.commit()
    conn.close()


def empty_db():
    conn = sqlite3.connect("repo_db")

    conn.execute("""DELETE FROM Tasks;""")

    conn.commit()
    conn.close()


class SQLiteRepository(Repository):
    def create(self, task: Task) -> None:
        conn = sqlite3.connect("repo_db")
        query = f"INSERT INTO Tasks (task_id,task_name,message) \
             VALUES ('{str(task.task_id)}', '{task.task_name.value}', '{task.message}' )"
        print(query)
        conn.execute(query)
        conn.commit()
        return None

    def read(self, task_id: uuid.UUID) -> Task:
        connection = sqlite3.connect("repo_db")
        cursor = connection.execute(
            f"SELECT task_id, task_name, message from Tasks where task_id = '{str(task_id)}'"
        )
        retrieved_tasks = []
        for row in cursor:

            retrieved_tasks.append(
                Task(**{"task_id": row[0], "task_name": row[1], "message": row[2]})
            )
        if len(retrieved_tasks) == 1:
            return retrieved_tasks[0]
        raise RepositoryExeption(f"Cannot find a Task with ID {task_id}")

    def update(self, task: Task) -> None:
        ...

    def delete(self, task: Task) -> None:
        ...

    def load(self) -> list[Task]:
        ...


if __name__ == "__main__":
    # setup_db()
    empty_db()
    repo = SQLiteRepository()
    for task in tasks:
        repo.create(task=task)
    print(repo.read(tasks[0].task_id))
