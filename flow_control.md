The Python flow control statements:

Program execution does not have to happen top-to-bottom. This is where flow-control comes in.

## if

The `if` clause is executed when the condition evaluates to `True`:

```python
if variable == 'condition':
    print('Execute if-clause')
```

The `if` statment can test for `True` without any comparison operator:

```python
if True:
    print('Execute if-clause')
```

## else

The `if` clause can be followed by an `else` statement. The `else` clause is executed when the `if` statement's condition is `False`:


```python
var = False
if var:
    print('Execute if-clause')
else:
    print('Execute else-clause')    
```

The `else` statement does not have a condition.

Can be written in a terse way:

```python
>>> var = False
>>> msg = 'if-clause' if var else 'else-clause'
>>> msg
'Execute else-clause'
```

## elif

Follows an `if` statement and provides another condition that is checked only if all of the previous conditions were False:

```python
age = 105
if age < 80:
    print('Execute if-clause')
elif age > 80 and age < 120:
    print('Execute elif-clause')    
else:
    print('Execute else-clause')    
```

## multiway branching using dictionaries

```python
def junos_cmd():
    return 'show interfaces terse'

def arista_cmd():
    return 'show ip interfaces brief'

mw_branch = {
    'juniper' : junos_cmd,
    'arista' : arista_cmd,
}
>> mw_branch['juniper']()
'junos cmd'
>> mw_branch['arista']()
'eos cmd'
```

## for loop

Steps through the items of an iterable object.

```python
some_list = [ 1, 2, 3, 4]
for item in some_list:               # Assign object items to target
    print(item)     
    if item == 2: continue            # Go to top of loop now
    if item > 5: break                # Exit loop now, skip else (set to 3 to observe)
else:
    print('execute else clause')     # No break
```

Can also iterate dictionaries:
```python
d = {
    'a' : 1,
    'b' : 2,
}
for key, value in d.items():
    print(key)
    print(value)
```

The built-in zip function returns a series of parallel-item tuples:
```python
some_list_1 = [1,2,3,4]
some_list_2 = [5,6,7,8]
list(
    zip(some_list_1, some_list_2)
    )
for (x, y) in zip(some_list_1, some_list_2):
    print(x, y, '--', x+y)
```
The above outputs the following:
```
[(1, 5), (2, 6), (3, 7), (4, 8)]

1 5 -- 6
2 6 -- 8
3 7 -- 10
4 8 -- 12
```

The built-in `enumerate` generates both the value as well as the index of the item in an iterable. Every time an (index, value) tuple is generated:

```python
string = "Python"
for (offset, letter) in enumerate(string): 	
    print(f'Letter {letter} appears at index {offset}', )
```

The above outputs:
```
Letter P appears at index 0
Letter y appears at index 1
Letter t appears at index 2
Letter h appears at index 3
Letter o appears at index 4
Letter n appears at index 5
```


## while (loop)


Repeatedly executes a block of statements as long as the while statement's condition is `True`:
```python
number = 0
while number < 6:                                   # while loop test
        print(f'Still going at {number}')           # start of the while loop body
        number = number + 1
        #if number > 2: break                       # uncommenting this line and else is not executed
else:                                               # optional else
    print("Executes if the loop did not break")     
```

Note that the loop `else` clause is also run if the body of the loop is never executed.


```python
while test:    
    statements    
    if test: break                 # Exit loop and skip else
    if test: continue              # Go to test at top of loop
else:
    statements                     # Run if we didn't hit a 'break'
```


## sys.exit()

The `sys.exit()` will raise a `SystemExit` exception. An argument can be passed to `sys.exit()` to signal an exit code. The default is `None` value used is, which translates to `0`.

```
[root@said /]# python -c "import sys; sys.exit()"; echo $?   
0
[root@said /]# python -c "import sys; sys.exit(0)"; echo $?
0
[root@said /]# python -c "import sys; sys.exit(123)"; echo $? 
123
```

```python
import sys
while True:	
	response = some_funcion()
	if response > 500:
		sys.exit(1)
```