
In Python, regular expressions are executed by a matching engine written in C. The `re` module is an interface to this matching engine.

| Method/Attribute   |             |
| ------------------ |:--------------:|
|  match()           | Determine the start of the match. |
|  search()          | Find (the first) match for the RE. |
|  findall()         | Returns a list of substrings where the RE matches. |
|  finditer()        | Returns an iterator that contains all substrings where the RE matches. |


| Method/Attribute   |	Purpose       |
| ------------------ |:--------------:|
| group() | Returns one or more subgroups of the match |
| groups() | Returns a tuple with all subgroups of the match |
| start() | Return the starting position of the match |
| end() | Return the ending position of the match |
| span() | Return a tuple containing the (start, end) positions of the match |


| Compilation flags	 |                |
| ------------------ |:--------------:|
| DOTALL, S	         | . will now match any character, including newlines |
| IGNORECASE, I	     | case-insensitive matches |
| MUTILINE, M	     | multi-line matching, affecting ^and $ |
| VERBOSE, X         | Verbose REs |


| Character          |             |
| ------------------ |:--------------:|
|  ?                 | Zero or one of the preceding |
|  *                 | Zero or more of the preceding |
|  +                 | One or more of the preceding |
|  {n}               | exactly n occurrences of the preceding |
|  {n,}              | n or more occurrences of the preceding |
|  {,m}              | 0 to m occurrences of the preceding |
|  {n,m}             | at least n and at most m occurrences of the preceding |
|  ^s                | Must start with s |
|  e$                | Must end with e |
|  .                 | any character except newline |
|  \d                | a digit |
|  \w                | a word (any letter, numeric digit or underscore) |
|  \s                | space, tab or newline character |
|  \D                | anything except a digit |
|  \W                | anything except a word |
|  \S                | anything except a space, tab or newline character  |
|  [abc]             | any characters between the brackets |
|  [^abc]            | any character that IS NOT between the brackets |


The `r` statement can be used to pass a raw string and avoids having to escape many characters.

## Examples

```python

string = """
Some words, characters, 9879286 2124.
"""

# Extracting the digits from the string:
#  1: Compile a regular expression pattern into a regular expression object:
#  2: Return a match object of the first location where there is a match:
#  3: Return one or more subgroups of the match:
po = re.compile(r'\d+')
mo = po.search(string)
mo.group()
>>> '9879286'

# Following is the same:
regex_result = re.search(r'\d+',string)
regex_result.group()
>>> '9879286'
re.search(r'\d+',string).group()
>>> '9879286'

# Using compilation flag:
paragraph = \
"""
<p>
Some text on a website.
Containing multiple lines.
</p>
"""

match = re.search(r'<p>.*</p>', paragraph, re.DOTALL)
match.group()
>>> '<p>\nSome text on a website.\nContaining multiple lines.\n</p>'

# Setting multiple compilation flags:
po = re.compile(r'<p>.*</p>', re.IGNORECASE | re.DOTALL | re.VERBOSE)
mo = po.search(paragraph)
mo.group()
>>> '<p>\nSome text on a website.\nContaining multiple lines.\n</p>'
# serach() versus findall():
re.search(r'\d', '0123456789').group()
>>> 0
re.findall(r'\d', '0123456789')
>>> ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# when groups are used, tuples are returned:
re.findall(r'(\d)(\d)', '0123456789')
>>> [('0', '1'), ('2', '3'), ('4', '5'), ('6', '7'), ('8', '9')]


# Carving out groups:
string = "blob of text 111-222-333 more text"

mo = re.search(r'(\d{3})-(\d{3})-(\d{3})', string,)

# mo now contains 3 groups
mo.group(0) # return all groups
mo.group() # return all groups
mo.groups()	# return all groups as a tuple
>>>
111-222-333
111-222-333
('111', '222', '333')

# return group 1,2 and 3
mo.group(1)
>>> '111'
mo.group(2)
>>> '222'
mo.group(3)
>>> '222'

# Assign multiple values at once:
mo = re.search(r'(\d{3})-(\d{3})-(\d{3})', string)
one, two, three = mo.groups()

# put in comments: 
mo = re.search(r'''
(\d{3}) # first group of numbers
-
(\d{3}) # seconds group of numbers
-
(\d{3}) # last group of numbers
''', string,)


# Pipe to match multiple groups.
re.search(r'Juniper|Cisco', 'Do you like Juniper or Cisco?').group()
>>>
Juniper

# Findall returns a list:
re.findall(r'Juniper|Cisco', 'Do you like Juniper or Cisco?') 
['Juniper', 'Cisco']

# match vowels:
re.findall(r'[aeiou]', 'come on come on come on now touch me babe')
>>> ['o', 'e', 'o', 'o', 'e', 'o', 'o', 'e', 'o', 'o', 'o', 'u', 'e', 'a', 'e']
# The opposite:
re.findall(r'[^aeiou]', 'come on come on come on now touch me babe')
>>> ['c', 'm', ' ', 'n', ' ', 'c', 'm', ' ', 'n', ' ', 'c', 'm', ' ', 'n', ' ', 'n', 'w', ' ', 't', 'c', 'h', ' ', 'm', ' ', 'b', 'b']

# greedy to non-greedy:
re.search(r'(\d){2,10}', '0123456789').group()
>>> '0123456789'

re.search(r'(\d){2,10}?', '0123456789').group()
>>> '01'

# sub method example:
# argument one: replacement.
# argument two: string to be pared.
# method return: string that has the substitution applied.

string = 'change this'
po = re.compile(r'this')
po.sub('that', string)
>>> 'change that'

```

