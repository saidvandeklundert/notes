# Repository pattern

The repository pattern is a strategy for abstracting data access. Simplifying abstraction over data storage allows us to decouple our model layer from the data layer.


The repository pattern has two purposes:
1. it is an abstraction of the data layer 
2. it is a way of centralizing the handling of the domain objects

The Repository Pattern has gained quite a bit of popularity since it was first introduced as a part of Domain-Driven Design in 2004. Essentially, it provides an abstraction of data, so that your application can work with a simple abstraction that has an interface approximating that of a collection. Adding, removing, updating, and selecting items from this collection is done through a series of straightforward methods, without the need to deal with database concerns like connections, commands, cursors, or readers. Using this pattern can help achieve loose coupling and can keep domain objects persistence ignorant.

Repository pattern best practices:
- implement CRUD operations: 
  - Create, Read, Update and Delete
- one repository per business object (single responsibility principle)
- provide a contract or interface
- use generic implementations

Benefits:
- makes it easier to test
- centralize common data access functionality
- abstracts datalayer, we no longer need to be concerned with low level implementation details:
  - easier to change the database backend
  - easier to reason about/change the domain models
- better flexibility, scalability and maintainability
- minimize duplicate query logic



Example:

```python
import abc
import model


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def create(self, router: model.router):
        raise NotImplementedError

    @abc.abstractmethod
    def read(self, router: model.router):
        raise NotImplementedError

    @abc.abstractmethod
    def update(self, router: model.router):
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, router: model.router):
        raise NotImplementedError



class SomeDatabase(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def create(self, router):
        self.session.add(router)
    
    # rest of the ABC


```
