from time import sleep
from concurrent.futures import ProcessPoolExecutor


def task():
    sleep(0.5)


if __name__ == "__main__":
    with ProcessPoolExecutor() as exe:
        future = exe.submit(task)

        future_running = future.running()
        future_status = future.done()
        print(
            f"Is the future running? {future_running}, is the future done? {future_status}"
        )

        future.result()

        future_running = future.running()
        future_status = future.done()
        print(
            f"Is the future running? {future_running}, is the future done? {future_status}"
        )
