## Open Closed Principle:


Code should be open to extension but closed to modification.

When we design classes, we need to think about the way we encapsulate the implementation details.


Detecting open closed principle violations:
- we should be able to extend the model/class without making changes to other parts. 

One way of adhering to the Open Closed Principe is to program against an abstraction, or an 'interface'.

Example:
```python
import json
import yaml
from abc import ABC, abstractmethod

class Serializer(ABC):
    @abstractmethod
    def serialize(self, dictionary: dict):
        """Serialize target dictionary."""


class YamlSerializer(Serializer):
    def serialize(self, dictionary: dict):
        print("serializing to YAML:")
        print(yaml.dump(dictionary))


class JsonSerializer(Serializer):
    def serialize(self, dictionary: dict):
        print("serializing to JSON:")
        print(json.dumps(dictionary))
```

It is easy to add new serializers without changing existing methods.