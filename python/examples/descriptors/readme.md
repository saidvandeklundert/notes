A descriptor is an object that is an instance of a class that implements the descriptor protocol. 

The descriptor protocol is implemented if the interface of a class contains at least one of the following magic methods:
- `__get__`
- `__set__`
- `__delete__`
- `__set_name__`