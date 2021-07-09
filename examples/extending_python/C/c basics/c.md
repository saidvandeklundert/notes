### Data types

`int`: variable that can be used to contain integral values only
`float`: numbers that contain decimal places
`double`: same as float but with roughly twice the precision. Used when the range of a float is not sufficient.

### Compiling

```
gcc 01.c
gcc -o 01.exe 01.c
```
### memory

`malloc`: allocate some memory

```c
b = (char *)malloc(size);
```

C does not include a garbage collector. You have to free the memory yourself using `free`:

```c
free(b);
```