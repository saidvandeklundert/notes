```python
>>> a, b, c = 0, 1, 0
>>> a == 1 or b == 1 or c == 1
True
>>> 1 in (a, b, c)
True
>>> a or b or c
1
>>> any((a, b, c))
True

# All the following will display yolo:
if a == 1 or b == 1 or c == 1:
    "yolo"

if 1 in (a, b, c):
    "yolo"

if a or b or c:
    "yolo"

if any((a, b, c)):
    "yolo"

```