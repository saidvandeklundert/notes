from functools import wraps
import time


def multiply(x: int, y: int) -> int:
    return x * y


def double(x: int) -> int:
    return multiply(x, 2)


def no_arg():
    return 3


def with_metadata(func, *args, **kwargs):
    """
    Take target function and add some metadata to the return of the wrapped
    function.
    """

    @wraps(func)
    def wrapped(*args, **kwargs):
        """
        The actual wrapper function that is adding the metadata.
        """
        function_name = func.__qualname__
        start_time = time.time()
        time.sleep(2)
        function_result = func(*args, **kwargs)
        duration = f"{time.time() - start_time:.2f}"

        return (function_result, function_name, args, kwargs, duration)

    return wrapped(*args, **kwargs)


@with_metadata
def double_annotated(x: int) -> int:
    return multiply(x, 2)


if __name__ == "__main__":
    print(with_metadata(multiply, 2, 3))
    print(with_metadata(double, 2))
    print(with_metadata(no_arg))
    try:
        print(double_annotated(x=2))
    except Exception as e:
        print(e)
        import pdb

        pdb.set_trace()
