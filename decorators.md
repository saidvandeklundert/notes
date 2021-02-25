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
```