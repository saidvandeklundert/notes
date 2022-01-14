#include <stdio.h>
/* count chars in input

ctrl-c ends the program*/

main()
{
    long nc;
    nc = 0;
    while (getchar() != EOF)
        ++nc;
    printf("%ld\n", nc);
}