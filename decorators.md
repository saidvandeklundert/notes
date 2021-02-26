# Decorators


```python
import functools

# The decorator:
def decorator(func):
    @functools.wraps(func)
    def run_func():
        print("Before the decorated function.")
        func()
        print("After the decorated function.")
    return run_func

# The decorated:
@decorator
def function():
    print("Example function.")

>>> function()
Before the decorated function.
Example function.
After the decorated function.


def decorator_w_args(number):
    def decorator(func):
        @functools.wraps(func)
        def func_running_func(*args, **kwargs):
            print("Before the decorated function.")
            if number < 100:
                print("False")
                return False
            else:
                print("Function")
                func(*args, **kwargs)
            print("After the decorated function.")
        return func_running_func
    return decorator

@decorator_w_args(101)   
def function(x, y):
    print(x, y)

>>> function(66, 77)
66 77
```