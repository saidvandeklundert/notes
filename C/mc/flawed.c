/* This may look like nonsense, but really is -*- mode: C -*- */
/* The main thing that this program does. */
#include <stdio.h>
int main()
{
    // Declarations
    int i;
    double A[5] = {
        9.0,
        2.9,
        3.E+25,
        .00007,
    };
    // Doing some work
    for (i = 0; i < 5; ++i)
    {
        printf("element %d is %g, \tits square is %g\n",
               i,
               A[i],
               A[i] * A[i]);
    }
    int people = 4;
    double x = (double)people;
    return 0;
}