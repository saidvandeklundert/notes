# Files

You use the built-in `open` function to interface with files. This function is passed a filename and an optional processing mode. The built-in open function then creates a Python file object that can be used to manipulate the file.

After using `open`, you can work with the file by interfacing with the returned file object’s methods. 
Files are considered a core type because they are created by a built-in function. 

When you are reading a file, using an iterator is most efficient.


| File processing mode  |             |
| ------------------ |:--------------:|
| 'r'                | read (default) |
| 'r+'               | reading and writing |
| 'w'                | write          |
| 'a'                | append         |
| 'a+'               | reading and appending |


### Working with files:

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

# Print file to screen:
print(open('example.txt').read())

# iterate lines in a file:
for line in open('example.txt'): print(line)

f.read()		# use the iteror to return one big string
f.readline()	# use the iterator to return one line at a time
f.readlines()	# use the iteror to return a list

# Context manager automatically closes file:
with open('example.txt', 'r') as f:
    print(f.read())
    f.close()
# Convention is to still use close.

# Write a string to a file:
f.write(string)

# Write a list of strings to a file:
x = ['a', 'b']
f.writelines(x)

# pformat returns the formatted representation of object as a string
import pprint

dictionary = {
    'r1' : '10.0.0.1',
    'r2' : '10.0.0.2',
    'r3' : '10.0.0.3',
}

with open('pformat_dict.py', 'w') as file:
    file.write(pprint.pformat(dictionary))
    file.close()


# List comprehending a file:
lines = [line.rstrip() for line in open('example.txt') if 'p' in line ]
```


### Working with files in directories:


```python
# Get the working directory:
os.getcwd()

# Change to another directory:
os.chdir('C:\\temp\\stuff')       
os.getcwd()
>>> 'C:\\temp\\stuff'

# True if file or folder exists, False otherwise:
path = 'C:\\temp\\stuff' 
os.path.exists(path)
>>> True

# True if the path + file exists, False otherwise:
os.path.isfile(path)

# True if path exists and if it is a folder, False otherwise:
os.path.isdir(path) 

# Files and folders as a list in cwd:
os.listdir() 


# Files and folders as a lit in target directory:
os.listdir(path)

# Return size of the file in bytes:
os.path.getsize(path)

# Total file size for all files in target dir
total = 0
for f in os.listdir(path):
    total += os.path.getsize(path + f)

path = 'C:\\temp\\stuff\\yolo.text'
# Get the file name:
>>> os.path.basename(path)        
'yolo.text'
# Get the dir name:
>>> os.path.dirname(path)  
'C:\\temp\\stuff'

# Create a directory:
os.mkdir('C:\\testing')

# Return a tuple with the filepath and the filename:
os.path.split(path)
>>> ('C:\\temp\\stuff', 'yolo.text')
```