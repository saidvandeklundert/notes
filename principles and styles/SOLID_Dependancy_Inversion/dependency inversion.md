## Dependancy inversion Principle (DIP):

Design principle that states that we should not depend on low-level implementations, but rather rely on high-level abstractions:
- high-level components should not import anything from low-level components; they should both depend on abstractions
- abstractions should not depend on concrete implementations; concrete implementations should depend on abstractions

On way of implementing dependancy inversion is by creating an interface for clients to adhere to. This opens up the door to more clients we want to add in the future: just create a new class that satisfy the interface. As an added bonus, the design is now open for extension and closed for modification.

Abstractions have to be organized in such a way that they do not depend on details, but rather the other way around—the details (concrete implementations) should depend on abstractions.

In general, we could expect concrete implementations to change much more frequently than abstract components. It is for this reason that we place abstractions (interfaces) as flexibility points where we expect our system to change, be modified, or extended without the abstraction itself having to be changed.

Why is it called dependancy inversion?

Consider the following two classes:

`Robot` - > `Laser`

Here, Robot depends on a Laser. Now we 'invert' it:

`Robot` - > `Weapons_interface` <- `Laser`

The Laser dependancy is 'inverted', it is now pointing the other way around to an interface.


## Dependancy injection:

This design pattern has us 'inject' any required objects at runtime. Components that have other components 'injected' into them do not have to worry about constructing them. 

This usually works hand in hand with dependancy inversion. For instance, we can use an interface to determine what can be injected into a software component. This way, we make the component depend upon an abstraction (the interface) while we inject the other component (dependancy injection).



## Examples:


```python
class EventStreamer:
    def __init__(self):
        self._target = Syslog()
    def stream(self, events: list[Event]) -> None:
        for event in events:
            self._target.send(event.serialise())
```
Here, the `EventStreamer` creates somethig of the type `Syslog`.

There are some downsides to this though:
- not very flexible
- does not take full advantage of an interface (we cannot change the `Syslog` elsewhere in our code)
- harder to test

Better would be 'giving' or 'injecting' the type like so:

```python
class EventStreamer:
    def __init__(self, target: DataTargetClient):
        self._target = target
    def stream(self, events: list[Event]) -> None:
        for event in events:
            self._target.send(event.serialise())
```
The advantages:
- we can pass anything that implements the interface
- it is very explicit that we use a type that implements an interface
- simpler to test (we can supply a test double)

We have also inverted the dependancy. Whatever we inject into the `EventStreamer` now has a dependancy on the interface.

## Bad:

The Robot builds all of the dependencies:

```python
@dataclass
class Laser:
    damage: int


@dataclass
class Robot:
    serial: str
    weapon: Laser


r2d2 = Robot(serial="r2d2", weapon=Laser(damage=21))
```

## Good:

Everything is constructed outside of Robot. The `Laser` has the dependancy inverted because it now depends on the interface. We also implement dependancy injection, since we inject the `Laser` into the robot:

```python
@dataclass
class Robot:
    serial: str
    weapon: Laser


class Weapon(ABC):
    @abstractmethod
    def shoot(self):
        pass


@dataclass
class Laser(Weapon):
    damage: int


@dataclass
class BFG(Weapon):
    damage: int




laser = Laser(damage=20)
r2d2 = Robot(serial="r2d2", weapon=laser)
```

Coming up with new weapons in the future is easy.