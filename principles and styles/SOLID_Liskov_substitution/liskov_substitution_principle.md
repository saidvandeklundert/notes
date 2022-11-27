## Liskov Substitution Principle (LSP):

LSP states that there is a series of properties that an objects must hold to preserve the reliability of its design.

Clients should be unaware of changes in the class hierarchy. More formally:

```
if S is a subtype of T, then objects of type T may be replaed by objects of type S without breaking the program.
```

The LSP is fundamental to good object-oriented software design because it emphasizes one of its core traits—polymorphism. It is about creating correct hierarchies so that classes derived from a base one are polymorphic along the parent one, with respect to the methods on their interface.

Abstract methods and properties are one way of enforcing LSP in Python. Protocols are another.
