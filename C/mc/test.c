/* This may look like nonsense, but really is -*- mode: C -*- */
/* The main thing that this program does. */
#include <stdio.h>
int main()
{
    // Declarations
    char letter = 'a';
    switch (letter)
    {
    case 'a':
        puts("a");

    case 'b':
        puts("b");
        // break;
    case 'c':
        puts("c");
        break;
    default:
        puts("something else, anything really");
    }
    return 0;
}