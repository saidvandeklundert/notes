// zig cc .\hello_world.c -o hello_world.exe
#include <stdio.h>
int main(int argcount, char **argv)
{
    printf("Hello world!\n");

    printf("Compiled using 'zig cc .\\hello_world.c -o hello_world.exe'");
    return 0;
}