#include <stdlib.h>
#include <stdio.h>

// Allocate memory for a static, which will
// live for the duration of the program.
int my_var = 80;


int main(){

    // dynamic allocation:
    int *x = malloc(sizeof(int));       // give me space for 1 int
    int *arr = malloc(sizeof(int) * 100); // give me space for 100 int's

    *x = 120;
    arr[90] - 0xFEEDBEEF;
    arr[101] = 9; // out of bounds!!!!

    free(arr); // free the allocated memory
    arr = NULL; // indicate this was freed

    double *darr;
    darr = calloc(sizeof(double),100);
    // same as malloc(sizeof(double) *100 );

    // we can resize calloc:
    darr = realloc(darr, sizeof(double) * 500);

}