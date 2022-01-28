https://docs.python.org/3/reference/datamodel.html#
https://docs.python.org/3/c-api/intro.html

Objects are Python’s abstraction for data. All data in a Python program is represented by objects or by relations between objects. (In a sense, and in conformance to Von Neumann’s model of a “stored program computer”, code is also represented by objects.). 

The type() function returns an object’s type (which is an object itself). 


Every object has an identity, a type and a value. An object’s identity never changes once it has been created; you may think of it as the object’s address in memory. The ‘is’ operator compares the identity of two objects; the id() function returns an integer representing its identity.

All Python objects (even Python integers) have a type and a reference count. When an object’s reference count becomes zero, the object is deallocated. If it contains references to other objects, their reference count is decremented. Those other objects may be deallocated in turn, if this decrement makes their reference count become zero, and so on. 

Reference counts are always manipulated explicitly. The normal way is to use the macro Py_INCREF() to increment an object’s reference count by one, and Py_DECREF() to decrement it by one.


