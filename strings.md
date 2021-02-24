Python strings are immutable sequences.


Common string operations:

```python
string_1 + string_2         # concatenate string
string_1 * 4                # repeat string
string_1[1]                 # get character at index 1
len(sring_1)                # return the lenght of the string

# Find the index of a substring
>>> 'string'.find('i')
3
>> 'string'.find('xxx') 
-1

# replace all occurences of a substring:
>>> 'string'.replace('str', 'STR_') 
'STR_ing'

# read the help for the method:
help('string'.replace())

# Split string on character:
>>> 'string'.split('i') 
['str', 'ng']

# Split string on newlines:
>>> 'Line 1.\nLine 2.\nLine 3.'.split('\n')  
['Line 1.', 'Line 2.', 'Line 3.']
# OR:
>>> 'Line 1.\nLine 2.\nLine 3.'.splitlines() 
['Line 1.', 'Line 2.', 'Line 3.']

# Check if string ends with substring:
>>> 'string'.endswith('str')   
False

# Check if string starts with substring:
>>> 'string'.startswith('str')
True

# sript whitespaces:
>>> '    string    '.rstrip()    
'    string'
>>> '    string    '.lstrip() 
'string    '
>>> '    string    '.strip()  
'string'

# upper and lower:
>>> 'string'.upper()
'STRING'
>>> 'STRING'.lower()
'string'

# True if string is all leters:
>>> 'string'.isalpha()                   
True
#isalnum(): returns True if the string consists of only letters and numbers and is not blank.
#isdecimal(): returns True if the string consists only of numeric characters and is not blank.
#isspace(): returns True if the string consists only of spaces, tabs and newlines and is not blank.
#istitle(): True if string consists of words that begin with an uppercase letter followed by lowercase letters only


# Joing several strings
>>> ' '.join(['Join', 'several', 'strings', '.']) 
'Join several strings .'

# membership check:
>>> 's' in 'string' 
True

# string in reverse:
>>> 'string'[::-1]
'gnirts'

# iterate string:
for c in 'string': print(c)

# String formating:
name = 'Said'
'my name is {}'.format(name)
f'my name is {name}.'
'my name is %s' % (name)
# all give:
>>> 'my name is Said'

# raw string (ignores all escape characters):
r= r'Router /s !@#$%^&*()'
>>> r
'Router /s !@#$%^&*()'

"""
Multine strings.
  with tabs and newlines.
"""

# Padding a string:
>>> string = 'router'
>>> string.rjust(10, '-')
'----router'
>>> string.ljust(10, '-')
'router----'
>>> string.center(10, '-')
'--router--'
```

Escape characters:
```python
"\’"              # single quote
"\""              # double quote
"\t"              # tab
"\n"             # newline
"\\"              # Backslash
```

String slicing examples are found [here](https://github.com/saidvandeklundert/python/blob/main/lists.md#list-and-string-slicing-examples).