# Hash Table: An Array With a Hash Function

Accessing elements in an array is fast because:
- an array occupies a contiguous block of memory
- where the size of the array is known in advance
- and every element in the array has a fixed size

Because of this, it is easy for a compuer to fetch the nth element. The memory address of the array is known. And when an element needs to be fetched, the computer calculates an offset.

Hash tables get heir name from something called `hashing`. This makes it possible to translate a key into an integer number. This number can constitute an index in a regular array.

Hash functions turn data into a fixed-size sequence of bytes that is called the `hash value` or `hash code`. This number, also known as a `digest`, is a lot smaller then the orignal data. It also allows you to verify the integrity of the data. There are many, many different `hashing algorithms`. 

Hash functions all repeatedly produce the same result over and over again and the resulting output has a fixed-size. This is because the input value to a hash function has to be `immutable`.

Because there is a fixed size to the output, and given the fact that the size is not infinite, hash collisions are a possibility. A hash collision is when 2 values produce the same hash result.

When there is talk of a cryptographic hash function, it will over a few security related features over a 'normal' hash function. Some of these could be that they include a randomized seed, they are a one-way function and they take into consideration the avalance effect.

Hashes can collide, leading to undesired behavior. There are a few strategies available to avoid hash collisions:
- `Closed Addressing`: store collisions in a separate datastructure (like a linked list for instance with [separate chaining](https://en.wikipedia.org/wiki/Hash_table#Separate_chaining)) to search through upon lookup.
- `Open Addressing`: spread  collided values in a predictable way so you can retrieve them later. Different algorithms are available to achieve this:
  - Cuckoo hashing
  - Double hashing
  - Hopscotch hashing
  - Linear probing
  - Quadratic probing
  - Robin Hood hashing
- `Perfect Hashing`: avoid hash collisions in the first place.



















Interesting articles/links:
[Understanding and implementing a Hash Table (in C)](https://www.youtube.com/watch?v=2Ti5yvumFTU)
[Realpython example](https://github.com/realpython/materials/tree/master/hashtable)
[Build a Hash Table in Python With TDD](https://realpython.com/python-hash-table/#build-a-hash-table-prototype-in-python-with-tdd)
[leetcode excercise](https://leetcode.com/problems/design-hashmap/)

[Brandon Rhodes: The Mighty Dictionary (PyCon 2010)](https://www.youtube.com/watch?v=oMyy4Sm0uBs)
[Brandon Rhodes The Dictionary Even Mightier PyCon 2017](https://www.youtube.com/watch?v=66P5FMkWoVU)
[Raymond Hettinger about the python dict](https://www.youtube.com/watch?v=p33CVV29OG8)


[Live-coding a linked hash map in Rust](https://www.youtube.com/watch?v=k6xR2kf9hlA)