

## Array:

Contiguous memory.

## Dynamic array a.k.k resizable array a.k.a ArrayList:

Backed by an array that can be resized as needed. Could be done as a struct that holds an array, a size and a capacity:

```c
typedef struct ArrayList {    
    int* array;
    int size;
    int capacity;    
} ArrayList;
```
Resize functions can be used to shrink or grow the array.


## ArrayBuffer:

An array where there is a head and a tail pointer into the index of the array:

[ 0 1 2 3 4 5 6 7 8 9 10]
    ^          ^
    |          |
   head       tail

The tail and the head can ring around, meaning the tail pointer can be at idx 2 and the head can be at idx 10.

Resizing can be done when