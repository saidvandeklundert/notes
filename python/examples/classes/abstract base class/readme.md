The primary goal of abstract base classes is to formalize the relationship between a parent class and a subclass.

The `__abstractmetods__` attribute reveals the abstract methods.

ABCs are implemented using metaclasses and decorators.

The ABCs only check for the presence of methods, it does NOT check their signature or proper implementation. You can use mypy for instance, to improve this.

[Raymond Hettinger «Build powerful, new data structures with Python's abstract base classes»](https://www.youtube.com/watch?v=S_ipdVNSFlo)