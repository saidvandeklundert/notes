# hashtable.py
from typing import Iterator, NamedTuple, Any, Union, List

# sentinal value to understand
# if a hash collision took place:
DELETED = object()


class Pair(NamedTuple):
    key: Any
    value: Any


class HashTable:
    def __init__(self, capacity: int = 1000, load_factor_threshold: float = 0.6):
        if capacity < 1:
            raise ValueError("Capacity must be >= 1.")
        if not (0 < load_factor_threshold <= 1):
            raise ValueError("Load factor must be a number between (0, 1]")

        self._pairs: Union[Pair, None] = capacity * [None]
        self._load_factor_threshold = load_factor_threshold

    def __len__(self) -> int:
        """Returns the number of key/value pairs that
        were added to the hashmap."""
        return len(self.pairs)

    def __setitem__(self, key: Any, value: Any):
        if self.load_factor >= self._load_factor_threshold:
            self._resize_and_rehash()

        for index, pair in self._probe(key):
            if pair is DELETED:
                continue
            if pair is None or pair.key == key:
                self._pairs[index] = Pair(key, value)
                break
        else:
            self._resize_and_rehash()
            self[key] = value

    def _resize_and_rehash(self):
        """
        Resize the hashtable by changing the capacity of
        the backing array.
        """
        copy = HashTable(capacity=self.capacity * 2)

        for key, value in self.pairs:
            copy[key] = value

        self._pairs = copy._pairs

    def __getitem__(self, key):
        for _, pair in self._probe(key):
            if pair is None:
                raise KeyError(key)
            if pair is DELETED:
                continue
            if pair.key == key:
                return pair.value
        raise KeyError(key)

    def __delitem__(self, key):
        for index, pair in self._probe(key):
            if pair is None:
                raise KeyError(key)
            if pair is DELETED:
                continue
            if pair.key == key:
                self._pairs[index] = DELETED
                break
        else:
            raise KeyError(key)

    def __contains__(self, key) -> bool:
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True

    def get(self, key, default=None) -> Any:
        try:
            return self[key]
        except KeyError:
            return default

    @property
    def capacity(self) -> int:
        """Returns the integer value that represents
        the capacity of the hashmap."""
        return len(self._pairs)

    @property
    def pairs(self) -> Any:
        """The '.items()' implementation of this
        Hashmap. Returns all pairs from the Hashmap."""
        return [pair for pair in self._pairs if pair not in (None, DELETED)]

    @property
    def values(self) -> List[Any]:
        return [pair.value for pair in self.pairs if pair not in (None, DELETED)]

    @property
    def keys(self):
        return {pair.key for pair in self._pairs if pair not in (None, DELETED)}

    def _index(self, key) -> int:
        """Determine the index of the backing array
        by calucalating the hash of the key.

        % len will limit the"""
        return hash(key) % self.capacity

    def __iter__(self) -> Iterator[Any]:
        yield from self._pairs

    def __str__(self) -> str:
        pairs = []
        for key, value in self.pairs:
            pairs.append(f"{key!r} : {value!r}")
        return "{" + ", ".join(pairs) + "}"

    @classmethod
    def from_dict(cls, dictionary, capacity=None):
        """Enable class construction from a dictionary,
        and from the output of repr."""
        hash_table = cls(capacity or len(dictionary))
        for key, value in dictionary.items():
            hash_table[key] = value
        return hash_table

    def __repr__(self):
        """Returns a string represenation of the
        syntax needed to create the instance of the HashTable."""
        cls = self.__class__.__name__
        return f"{cls}.from_dict({str(self)})"

    def __eq__(self, other):
        if self is other:
            """If id is the same, return True"""
            return True
        if type(self) is not type(other):
            """If the type is not the same, things cannot be equal."""
            return False
        return set(self.pairs) == set(other.pairs)

    def copy(self):
        """Generate a copy of an instance of the HashTable"""
        return HashTable.from_dict(dict(self.pairs), self.capacity)

    def _probe(self, key: Any):
        index = self._index(key)
        for _ in range(self.capacity):
            yield index, self._pairs[index]
            index = (index + 1) % self.capacity

    @property
    def load_factor(self) -> int:
        """The load factor is the ratio of occupied and deleted slots
        to all the slots in the table.

        The higher the load factor, the more likely it is a collision
        will occur."""

        occupied_or_deleted = [slot for slot in self._slots if slot]
        return len(occupied_or_deleted) / self.capacity


if __name__ == "__main__":

    hash_table = HashTable(capacity=100)
    hash_table["example_key"] = "example_value"
    hash_table[1001] = 101
    hash_table[False] = True
    hash_table[100] = 101
    hash_table.pairs
    # collisions ^

    # no collisions:
    h_t = HashTable(capacity=100000)
    h_t["example_key"] = "example_value"
    h_t[1001] = 101
    h_t[False] = True
    h_t[100] = 101
    h_t.pairs
    print(h_t)
