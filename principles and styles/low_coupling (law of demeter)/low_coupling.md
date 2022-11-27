
Be cognisant of the coupling in your programs.

## Principle of least knowledge / law of Demeter:

Strive to only having units that know about and/or talk to units that are closely related.

## Types of coupling:

Coupling is not always a bad thing. Understanding and reasoning about the different types of coupling is very helpful.

`content coupling`: one method, function or class that is modifying data directly in another class.

`global coupling`: happens when functions share global data.

`external coupling`: when your application communicates with an external API.

`control coupling`: when one module or part of the code controls the flow of another module or part of the code. For instance, passing a function into a search method. 

`stamp coupling`: data structures being coupled even when this is not needed. For instance, depending on the dictionary keys without depending on the values of that dictionary (which might be complicated structs). You depend on the structs that you do not need.

`data coupling`: when multiple functions all rely on the same struct.

`import coupling`: relying on pandas for instance.

`message coupling`: depending on messages that pass data around (very weak form of coupling).