# Files



| File processing mode  |             |
| ------------------ |:--------------:|
| 'r'                | read (default) |
| 'w'                | write          |
| 'a'                | append         |
| 'a+'               | read and write |



```python
# Open file and write to it:
f = open('example.txt', 'w')      
f.write('Hello\n')             
f.write('world.\n') 
f.close()

# Open file and read from it:
f = open('example.txt', 'r') 
f.read()
>>> 'Hello\nworld.\n'
f.close()

# iterate lines in a file:
for line in open('example.txt'): print(line)

f.read()		# returns one big string
f.readline()	# returns one line at a time
f.readlines()	# returns a list of lines

# Context manager automatically closes file:
with open('example.txt', 'r') as f:
    print(f.read())
    f.close()
# Convention is to still use close.
```