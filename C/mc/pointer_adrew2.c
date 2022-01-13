#include <stdio.h>
#include <string.h>
#include <stdlib.h>
struct demo
{
    int a, b;
};
int main()
{
    // Create 20 demo structs in an array - example1 is a pointer
    struct demo example1[20];
    // Create a pointer and allocate memory for 20 demo structs
    struct demo *example2 = calloc(20, sizeof(struct demo));
    // example1 and example2 are now the same size in memory

    // Set array position 5 in example1 with a = 10 and b = 20
    example1[5].a = 10;
    example1[5].b = 20;
    // Do the same thing in example2 array - this time using pointer alignment
    (example2 + 5)->a = 30;
    (example2 + 5)->b = 40;
    // Print both
    printf("Example1[5] - a: %d b: %d\n", example1[5].a, example1[5].b);
    printf("Example2 element 5 - a: %d b: %d\n", (example2 + 5)->a, (example2 + 5)->b);

    // Copy example1 element 5 to example2 element 6
    // Note - example1[5] is not a pointer, so you have to reference it
    memcpy((example2 + 6), &example1[5], sizeof(struct demo));

    // Now copy example1 element5 to example2 element 7 - using pointer maths entirely
    memcpy((example2 + 7), (struct demo *)(example1 + 5), sizeof(struct demo));

    printf("Example2 ELement 6: a: %d b: %d\n", example2[6].a, example2[6].b);
    printf("Example2 ELement 7: a: %d b: %d\n", example2[7].a, example2[7].b);
}