#include <stdio.h>
#include <string.h>
int main()
{
    // Array of 500 characters - blah is actually a pointer to 500 bytes of allocated memory
    char blah[500];
    // Create demo - unassigned pointer
    char *demo;
    // Point demo at the same memory that blah is pointed to
    demo = blah;
    // Zero it out
    memset(blah, 0, 500);
    // Print some garbage into the memory pointed at by blah
    snprintf(blah, 500, "Printing crap into a string");
    // Both of these print the same thing
    printf("%s\n", blah);
    printf("%s\n", demo);
    snprintf(demo + 10, 400, "Demo of offset...\n");
    printf("%s\n", blah);
    printf("Using '&var': memory address of 'demo': %x\n", &demo);
    printf("Using '&var': memory address of 'blah': %x\n", &blah);

    printf("Value of the pointer *demo: %s\n", *demo);
    printf("Value of the pointer *blah: %s\n", *blah);
    return 0;
}