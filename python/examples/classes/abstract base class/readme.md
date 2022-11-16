The primary goal of abstract base classes is to formalize the relationship between a parent class and a subclass.


The ABCs only check for the presence of methods. It does NOT check their signature or whether or not the impelementation was done properly. You could use mypy to improve this.

ABCs are not meant to be instantiated, rather, they define a contract that other classes should adhere to. In other languages, this is sometimes called 'interface'.


ABC: for nominal typing. If you want a typing relation to be there, you write it down explicitly using inheritence.

Protocols is used for structural typing: instead of stating it explicitly, Python examines the structure of the objects. If they have the same methods/properties, then it is assumed that the types match. There is no inheritence with protocols. Rather, an interface is specified.

When there are multiple interfaces that can apply to a closs, protocols might be better. Structural typing can be applied without having using multiple inheritence.

ABCs are hierarchical
Protocols blon

## Technicalities

The `__abstractmetods__` attribute reveals the abstract methods.

ABCs are implemented using metaclasses and decorators.

[Raymond Hettinger «Build powerful, new data structures with Python's abstract base classes»](https://www.youtube.com/watch?v=S_ipdVNSFlo)