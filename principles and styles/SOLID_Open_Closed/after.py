"""
In this case, we change the serializer to an interface.

We can easily extend the code with another serializer. We do this
 by making another class that satisfies the interface.
"""
from abc import ABC, abstractmethod
from typing import Dict
import yaml
import json

TO_SERIALIZE = {1: "one", 2: "two", 3: ["1", "2", "3"]}


class Serializer(ABC):
    @abstractmethod
    def serialize(self, dictionary: Dict):
        """Serialize target dictionary."""


class YamlSerializer(Serializer):
    def serialize(self, dictionary: Dict):
        print("serializing to YAML:")
        print(yaml.dump(dictionary))


class JsonSerializer(Serializer):
    def serialize(self, dictionary: Dict):
        print("serializing to JSON:")
        print(json.dumps(dictionary))


if __name__ == "__main__":
    yaml_serializer = YamlSerializer()
    yaml_serializer.serialize(TO_SERIALIZE)

    json_serializer = JsonSerializer()
    json_serializer.serialize(TO_SERIALIZE)
