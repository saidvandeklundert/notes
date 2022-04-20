"""
Open for extension, closed for modification.


Next example is not good because if we want to add a serializer,
 like JSON, we would have to modify the existing class.

Either we would have methods with different names (yaml_serializer, json_serializer) 
or we put 'if' statements in existing methods.
"""
from typing import Dict
import yaml

TO_SERIALIZE = {1: "one", 2: "two", 3: ["1", "2", "3"]}


class Serializer:
    def serialize(self, dictionary: Dict):
        print("serializing to YAML:")
        print(yaml.dump(dictionary))


if __name__ == "__main__":
    serializer = Serializer()
    print(serializer.serialize(TO_SERIALIZE))
