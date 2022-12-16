The general idea of a decorator is that it creates a function that returns another function. The decorators wraps around and executes the decorated function.

In a sense, this turns the decorator into a higher-order function.

Little known fact is that a Python decorator can decorate classes as well as functions. Additionally, the decorator itself can be implemented as a function or as a class.
    
Reasons for using decorators:
- trace code:
  - log messages
  - time the operation and send the measurments somewhere
  - logging to other apps
- implement retry operations
- simplify classes by moving repetitive logic into a decorator, following the DRY principle
- transform parameters
- validate parameters
- interface with certain functions and classes that require a ton of parameters:
  - using decorators we can implement `partial`
  - a decorator can be used to implement the adaptor design pattern. We have the decorator
    supply most of the arguments, simplifying and or changing the way we interface with
    some complex object or module


Tips when using decorators:
- decorate the wrapper with `@functools.wraps`
- be wary of side-effects
- place the things the decorator does in the inner function that wraps around the function that is to be executed
- consider named args and kwargs versus unnamed ones as that favours readability


When implementing decorators:
- separate what it does and what it is decorating
- Clients invoking the decorator should be able to do so without knowing how it is implementing its logic
- what the decorator does should be independent from the object it is decorating
- it has to be generic and applicable to multiple functions
- provide a clean interface so that users know what to expect from the decorator, without having to know how it works