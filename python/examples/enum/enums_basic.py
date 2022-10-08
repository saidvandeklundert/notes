from enum import Enum


class Day(Enum):  # Enum or Enumeration
    MONDAY = "Monday"  # Enum member
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"


for day in Day:
    print(day)  # Day.MONDAY
    print(day.value)  # Monday

for day in Day.__members__:
    print(day)  # MONDAY

Day.MONDAY
Day("Monday")
Day["MONDAY"]

Day.MONDAY.name  # 'MONDAY'
Day.MONDAY.value  # 'Monday'

# can be a dict key:
some_d = {Day.MONDAY: 1, Day.FRIDAY: "some other value"}
print(some_d[Day.MONDAY])

# Can be empty:
class Empty(Enum):
    ...


# can be instantiated in different ways:
class HTTPMethod(Enum):
    GET = 1
    POST = 2
    PUSH = 3
    PATCH = 4
    DELETE = 5


HTTPMethodAlternative = Enum("HTTPMethod", ["GET", "POST", "PUSH", "PATCH", "DELETE"])

HTTPMethod.GET
HTTPMethodAlternative.GET

# The Enum-API offers even more options, including the use of name-value tuples upon instantiation:
HTTPStatusCode = Enum(
    value="HTTPStatusCode",
    names=[
        ("OK", 200),
        ("CREATED", 201),
        ("BAD_REQUEST", 400),
        ("NOT_FOUND", 404),
        ("SERVER_ERROR", 500),
    ],
)

# auto assign can offer some convenience:
from enum import auto, Enum


class Month(Enum):
    JANUARY = auto()
    FEBRUARY = auto()


print(list(Month))

# start at a different number:


class CardinalDirection(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name[0]

    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()


print(list(CardinalDirection))


# aliases:
from enum import Enum


class OperatingSystem(Enum):
    UBUNTU = "linux"
    MACOS = "darwin"
    WINDOWS = "win"
    DEBIAN = "linux"


# Aliases aren't listed
list(OperatingSystem)
# [
#    <OperatingSystem.UBUNTU: 'linux'>,
#    <OperatingSystem.MACOS: 'darwin'>,
#    <OperatingSystem.WINDOWS: 'win'>
# ]

# To access aliases, use __members__
list(OperatingSystem.__members__.items())
# [
#    ('UBUNTU', <OperatingSystem.UBUNTU: 'linux'>),
#    ('MACOS', <OperatingSystem.MACOS: 'darwin'>),
#    ('WINDOWS', <OperatingSystem.WINDOWS: 'win'>),
#    ('DEBIAN', <OperatingSystem.UBUNTU: 'linux'>)
# ]


from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


Color["RED"]
Color(1)


def handle_color(color: Color):
    if color is Color.BLUE:
        return "Blue"
    else:
        return "not Blue"


def handle_semaphore(light):
    match light:
        case Color.RED:
            print("You must stop!")
        case Color.YELLOW:
            print("Light will change to red, be careful!")
        case Color.GREEN:
            print("You can continue!")
