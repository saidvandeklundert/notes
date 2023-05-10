from concurrent.futures import ProcessPoolExecutor
import time


def write_to_file(num: int) -> None:
    time.sleep(10)
    with open(f"zz{num}.txt", "w") as f:
        print("yolo", file=f)


def fire_and_forget():
    executor = ProcessPoolExecutor()
    [executor.submit(write_to_file, number) for number in range(4)]
    executor.shutdown(wait=False)


if __name__ == "__main__":
    print("launch fire and forget")
    fire_and_forget()
    print("The program continues to do other stuff")
    print("fin")
    # the processes complete on their own
