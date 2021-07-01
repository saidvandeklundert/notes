from multiprocessing import Process, Lock, Queue
from random import randrange
import time


def safe_print(lock, *args):
    """acquire a lock, print and then release the lock"""
    lock.acquire()
    print(*args)
    lock.release()


def gather_info(lock, queue):
    """gathers information and puts the information on the Queue"""
    for x in range(0, 10):
        info = f"{x + 1}"

        safe_print(lock, "Obtained information:", info)
        queue.put(info)

        if randrange(1, 100) < 35:
            time.sleep(0.1)

    queue.put("finished")


def process_info(lock, queue):
    """processes information on the Queue until 'finished' is gotten off the queue"""
    info = queue.get()

    while info != "finished":
        safe_print(lock, "processing information:", info)
        info = queue.get()


if __name__ == "__main__":
    lock = Lock()
    queue = Queue()
    # both processes are given the same lock and the same queue:
    p1 = Process(target=gather_info, args=(lock, queue))
    p2 = Process(target=process_info, args=(lock, queue))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
