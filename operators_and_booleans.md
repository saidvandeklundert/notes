# Operators and Booleans.

Expressions consist of values and operators. They evaluate down to a single value.

Example:
5 + 5 evaluates down to 10

The `5`'s are the values and the `+` is the operator.

A single value with no operators is also considered an expression.


| Operator      | Operation             | 
| ------------- |:---------------------:|
| **            | exponent              |
| *             | multiplication        |
| /             | division              |
| //            | integer division      |
| %             | modulus/remainder     |
| +             | addition              |
| -             | subtraction           |

The above table is also the order of evaluation.

The Boolean (George Boole) has two values: True and False. 

| Identify operator      | Operation                         | 
| ---------------------- |:---------------------------------:|
| is                     | True if vars point to same object, False otherwise |
| is not                 | False if vars point to the same object, True otherwise    |

| Comparison operator    |                                   | 
| ---------------------- |:---------------------------------:|
| ==                     | Equal to |
| !=                     | Not equal to |
| <                      | Less than |
| >                      | Greater than |
| <=                     | Less than or equal to |
| >=                     | Greater than or equal to |

```python
== # compares the values of objects
is # compares the identity
```

| Boolean operator    |                                   | 
| ---------------------- |:---------------------------------:|
| and                     | Both must be True for the expression to be True |
| or                    | One must be True for the expression to be True |
| not                     | If the expression is True, it returns False. If the expression is False, it returns True |


| Expression    | Evaluates to |
| --------------- |:----------:|
| True and True   |	True       |
| True and False  |	False      |
| False and True  |	False      |
| False and False |	False      |

| Expression     | Evaluates to |
| -------------- |:-----------:|
| True or True   |	True       |
| True or False  |	True       |
| False or True  |	True       |
| False or False |	False      |

| Expression     | Evaluates to |
| -------------- |:-----------:|
| not True       |	False      |
| not False      |	True       |

| Expression     | meaning                                 |
| -------------- |:---------------------------------------:|
| x ^ y          |	Bitwise XOR, set symmetric difference      |
| x & y          |	Bitwise AND, set intersection       |