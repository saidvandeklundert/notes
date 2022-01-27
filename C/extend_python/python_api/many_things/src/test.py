"""
pip install -e src/
python3 src/test.py
"""
import many
from sys import getsizeof

name = many.Custom(first="Jan", last="van de Klundert")
print(name.name())
import array

a = array.array()
