#include <stdio.h>
/*
ctrl+d to exit on linux
ctrl-z to exit on windows

If you do not do the above, you will not see anything printed to screen.
*/
main()
{
    int c, i, nwhite, nother;
    int ndigit[10];

    nwhite = nother = 0;
    for (i = 0; i < 10; ++i)
        ndigit[i] = 0;

    for (i = 0; i < 10; ++i)
        printf(" %d", ndigit[i]);
    while ((c = getchar()) != EOF)
        if (c >= '0' && c <= '9')
            ++ndigit[c - '0'];
        else if (c == ' ' || c == '\n' || c == '\t')
            ++nwhite;
        else
            ++nother;

    printf("digits =");

    for (i = 0; i < 10; ++i)
        printf(" %d", ndigit[i]);

    printf(", whitespace = %d, other = %d\n",
           nwhite, nother);
}