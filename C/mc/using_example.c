/*
    This includes another file and uses the functions from that file.

    It includes the `example.h` file. In that file,
     the function `example` is defined. The source for this
     function is in `example.c`.

    In this directory, using gcc, you can compile the program as follows:

    $ gcc -o using_example.exe using_example.c example.c

    After this, run the program using '.\using_example.exe'
*/
#include <stdio.h>
#include "example.h"

int main(void)
{
    int y = example(3); /* Use the function here */
    printf("%d\n", y);
    return 0;
}