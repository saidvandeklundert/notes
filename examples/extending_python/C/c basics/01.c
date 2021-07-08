#include <stdio.h>
#include <math.h>

/*
    Multiline 
        comment
*/
#define MONDAY "Monday"                  // Old way, can be redefined elsewhere
static const char TUESDAY[] = "Tuesday"; // 'new' way

// a function:
void function_example()
{
    printf("running a func\n");

    // Using a constant from the math package:
    printf("%.10f\n", M_PI);
    // print 2 constants:
    printf("%s\n%s\n", MONDAY, TUESDAY);
}

int main(int argcount, char **argv)
{
    printf("hello world.\n");
    // for loop
    int i;
    for (i = 0; i < argcount; i++)
    {
        printf("Hello World again. argc = %d arg %d is %s\n", argcount, i, argv[i]);
    }
    function_example();

    return 0;
}