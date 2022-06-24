#include <stdio.h>
#include <string.h>

struct point {
    int x;
    int y;
};

typedef struct point point;

point *create_point(int x, int y){
    point p;
    p.x = x;
    p.y = y;
    printf("Created a point with x: %d and y: %d with the following memory address: %p\n", p.x, p.y, &p);
    return &p;
}

int main()
{

    int var = 100; /* declaring an integer value */
    int *ip;       /* declaring an integer pointer */

    ip = &var; /* store address of var in pointer variable*/

    printf("Using '&var': memory address of 'var': %x\n", &var);
    printf("Using 'ip': address value stored in the integer pointer: %x\n", ip);
    printf("Using '*ip': value of the integer pointer, retrieved using *ip: %d\n", *ip);

    // declare to variables that are of the type 'pointer to human':
    point* p1;

    p1 = create_point(3,4);    
    printf("Created a point with x: %d and y: %d with the following memory address: %p\n", p1->x, p1->y, p1);
    return 0;
}