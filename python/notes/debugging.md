## pdb & ipdb


Start (i)pdb inside a python script:

```python
# start trace:
import pdb; pdb.set_trace()
import ipdb; i-pdb.set_trace()

```

Great tip: when you are in (i)pdb, enter `interact`. The regular pdb takes you to a Python interpretor and you can issue multiline statements.

```python
(Pdb) interact
*interactive*
>>>
```

When using ipdb, you will enter iPython:

```
ipdb> interact
*interactive*
In :
```

### (i)pdb usefull commands:

`Stepping`:

```
n (next)        step over
s (step)        step into
r (return)      continue untill current function returns
c (cont.)       continue untill next breakpoint
j line_no       jump to line number
```

`Frame Navigation`:
```
u       up one level in the stack
d       down one level in the stack
```

`Display`:

```
p       print the value of an expression
pp      pretty print the value of an expression
w       pprint the current position and stack trace
l       list the lines of code around the current line
a       print the args of the current function
```

### pdbr for prettier debugging and extra's

https://github.com/cansarigol/pdbr

Some info came from Kapeli/cheatsheets, right [here](https://github.com/Kapeli/cheatsheets/tree/master/cheatsheets).
Visit the [page](https://kapeli.com/cheat_sheets/Python_Debugger.docset/Contents/Resources/Documents/index).

Nice pycon talk: [Goodbye Print, Hello Debugger! - Nina Zakharenko - Talk](https://www.youtube.com/watch?v=5AYIe-3cD-s).