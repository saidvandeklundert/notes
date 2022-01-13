#include <stdio.h>

int main()
{

    int var = 100; /* declaring an integer value */
    int *ip;       /* declaring an integer pointer */

    ip = &var; /* store address of var in pointer variable*/

    printf("Using '&var': memory address of 'var': %x\n", &var);
    printf("Using 'ip': address value stored in the integer pointer: %x\n", ip);
    printf("Using '*ip': value of the integer pointer, retrieved using *ip: %d\n", *ip);

    return 0;
}