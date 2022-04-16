from dataclasses import dataclass


@dataclass
class Human:
    name: str

    @property
    def name_length(self):
        return len(self.name)

    @property
    def name_len_squared(self):
        name_length = self.name_length
        return name_length * name_length


if __name__ == "__main__":
    me = Human(name="said")
    print(me.name_length)
    print(me.name_len_squared)
