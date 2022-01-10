#include <stdio.h>

/* function that adds 2 integers and returns an integer */
int add(int a, int b)
{
    int c;
    c = a + b;
    return c;
}

int main()
{
    int a = 10, b = 20;
    int c = add(10, 20); //function call
    printf("Addition:%d\n", c);
    return 0;
}
