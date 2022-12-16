## Chain of responsibility

Think pipelining. Nice to setup a chain of tasks that need to run. Can make it easy to schedule, manage and parallalize the tasks.

In this pattern, there is an interface for a handler. This interface has 2 methods:
- one to set a next hander
- one to execute an operation / task

The method to set a next handler is what helps build and setup the pipeline. The next handler sets a pointer to a possible next handler, sort of like in a linked-list.

The handle method is what executes the task/operation.

Example:
```python
class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass

```

Luigi and airflow packages can be used as pipelines.