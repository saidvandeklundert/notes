A descriptor is an object that is an instance of a class that implements the descriptor protocol. So implementing descriptors requires at least two classes. A client class that takes advantage of the functionality, and the descriptor class that is the implementation of the descriptor itself.

The descriptor is an object that is an instance of a class that implements the descriptor protocol. The descriptor protocol is implemented if the interface of a class contains at least one of the following magic methods:
- `__get__`
- `__set__`
- `__delete__`
- `__set_name__`

Example:

```python
class DescriptorClass:
    def __get__(self, instance):
        # performing some descriptor business
        return instance


class ClientClass:
    descriptor = DescriptorClass()
```

For the descriptor to properply work, it has to be implemented as a class attribute.

## So the descriptor is implemented, then what?!

A normal situation is displayed below. There, a class that accesses an attribute of itself of of one of the nested classes it contains, will simply have the attribute returned:

```python
class SomeAttribute:
    value = 421
 
class SomeClass:
    some_attribute = SomeAttribute()
```

```python
>>> SomeClass().some_attribute
<__main__.SomeAttribute object at 0x...>
>>> SomeClass().some_attribute.value
421
```

But, in the case of descriptors, something different happens. When an object is defined as a class attribute (and this one is a descriptor), when a client requests this attribute, instead of getting the object itself (as we would expect from the previous example), we get the result of having called the __get__ magic method.

When an object is defined as a class attribute, and it is a descriptor, this behavior is changed. When the attribute is requested, instead of getting the object itself, we get the result of the implemented `__get__` method of the descriptor. This could mean we get the object with some additional behavior or something else entirely.