"""
Why use class decorators?
- apply DRY principle by putting logic in a decorator and applying it to multiple classes
- use the decorator to enforce an interface or by writing checks
- can create a small and simple class that can be enhance later
- transformation logic applied using decorator can be more easy to maintain when compared to using meta-classes

"""
from dataclasses import dataclass
from datetime import datetime


def hide_field(field) -> str:
    """return redacted instead of the value of field"""
    return "**redacted**"


def format_time(field_timestamp: datetime) -> str:
    """change the fomatting of the timestamp"""
    return field_timestamp.strftime("%Y-%m-%d %H:%M")


def show_original(event_field):
    """Do not alter formattig."""
    return event_field


class EventSerializer:
    def __init__(self, serialization_fields: dict) -> None:
        self.serialization_fields = serialization_fields

    def serialize(self, event) -> dict:
        return {
            field: transformation(getattr(event, field))
            for field, transformation in self.serialization_fields.items()
        }


class Serialization:
    """Decorator for a class that alters the class
    by adding the 'serialize_method', which alters the way
    in which the class formats fields when serializing.

    Something that can be re-used accross many classes.

    Reason as to why this should be a decorator is that you can add methods
    to a class this way.
    """

    def __init__(self, **transformations):
        self.serializer = EventSerializer(transformations)

    def __call__(self, event_class):
        def serialize_method(event_instance):
            return self.serializer.serialize(event_instance)

        event_class.serialize = serialize_method
        return event_class


@Serialization(
    username=str.lower,
    password=hide_field,
    ip=show_original,
    timestamp=format_time,
)
@dataclass
class LoginEvent:
    username: str
    password: str
    ip: str
    timestamp: datetime


if __name__ == "__main__":
    event = LoginEvent(
        username="SAID", password="PASSWORD", ip="192.168.1.1", timestamp=datetime.now()
    )
    print(vars(event))
    print(event.serialize())
    type(event)  # __main__.LoginEvent
    dir(event)
    """
    [   
        'ip',
        'password',
        'serialize',
        'timestamp',
        'username'
    ]    
    """
