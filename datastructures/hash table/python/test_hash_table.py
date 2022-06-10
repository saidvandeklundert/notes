"""
python -m pytest test_hash_table.py
python -m mypy hash_table.py
"""
from hash_table import HashTable


def test_insert_key_value():
    hash_table = HashTable(capacity=100)

    hash_table["example_key"] = "example_value"
    hash_table[1001] = 101
    hash_table[False] = True

    assert ("example_key", "example_value") in hash_table.pairs
    assert (1001, 101) in hash_table.pairs
    assert (False, True) in hash_table.pairs


def test_delete_key_value_pair():
    hash_table = HashTable(capacity=100)
    hash_table["example_key"] = "example_value"
    assert "example_key" in hash_table
    del hash_table["example_key"]

    assert "example_key" not in hash_table
    assert ("example_key", "example_value") not in hash_table.pairs


def test_insert_none_value():
    hash_table = HashTable(1000)
    hash_table["key_to_none"] = None
    assert ("key_to_none", None) in hash_table.pairs


def test_capacity_hash_table_length():
    hash_table = HashTable(capacity=100)
    hash_table["example_key"] = "example_value"
    assert hash_table.capacity == 100
    assert len(hash_table) == 1


def test_equality():
    ht_1 = HashTable(capacity=100)
    ht_1["example_key"] = "example_value"
    ht_1["1"] = "1"
    ht_1["2"] = "2"

    ht_2 = HashTable(capacity=100)
    ht_2["example_key"] = "example_value"
    ht_2["1"] = "1"
    ht_2["2"] = "2"
    assert ht_1 == ht_2
