## Template Method Pattern

The template Method Pattern allows you to separate an algorithm from its parts.


The Template Method Pattern is cut from the same cloth as the Strategy Pattern, but it takes a different angle. With the Strategy Pattern, we can replace the algortihm and re-use the other parts of a software object. 

With the Template Method Pattern, we define the structure of the software object and give it a strategy. Other software objects can replace the structure with something else, but the algorithm stays the same.

The template method brings cohesion to everything that executes a similar pattern and it aids in applying the DRY principle, where you do not have to copy over teh structure again and again.

Consider using the Template Pattern when you have one (large) main algorithm with a lot of small varieties. What you do then is put the main algorithm in the parent class and define an interface for the varieties. All variants inherit the main class and then satisfy the interface.
