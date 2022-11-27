# from Clean code in Python
import contextlib


def stop_database():
    print("stop database")


def start_database():
    print("start datbase")


def db_backup():
    print("create datbase backup")

"""
Everything before the yield statement will be run
as though it was part of the __enter__ method.

Everything that comes after the yield statement can be
 considered part of the __exit__ method.S
"""
@contextlib.contextmanager
def db_handler():
    try:
        stop_database()
        yield
    finally:
        start_database()


with db_handler():
    db_backup()


"""
python .\using_context_lib.py
    stop database
    create datbase backup
    start datbase        
"""


# alternative:
class dbhandler_decorator(contextlib.ContextDecorator):
    def __enter__(self):
        stop_database()
        return self
    def __exit__(self, ext_type, ex_value, ex_traceback):
        start_database()

@dbhandler_decorator()
def offline_backup():
    print("pg_dump database")

# automatically runs inside a context manager.