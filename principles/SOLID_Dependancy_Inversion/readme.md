Inversion of control is a software development principle that encourages us to decouple components from their dependencies by supplying them at runtime. This allows us to control how the dependencies are supplied.

One popular pattern to accomplish this is the Dependancy Injection. Dependency injection is a software development patter where we supply code dependencies at runtime. This helps us decouple our components from the specific implementation details of the code they depend on, since they do not need to know how to configure and instantiate their dependencies.


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

Everything is constructed outside of Robot, inverting the dependancy. Also, it is easy to swap out weapons without ever even touching Robot:

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