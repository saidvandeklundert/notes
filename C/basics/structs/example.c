#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
struct Human
{
    char name[25];
    int age;
};

typedef struct Person
{
    char firstname[40];
    char lastname[40];
    int age;
    bool alive;
} Person;

int main()
{
    struct Human jan;
    jan.age = 6;

    memcpy(&jan.name, "Jan\0", 25);

    Person me = {.firstname = "John\0",
                 .lastname = "McCarthy\0",
                 .age = 24,
                 .alive = 1};
    printf("Name: %s\nLast Name: %s\nAge: %d\nAlive: ",
           me.firstname, me.lastname, me.age);
    printf("\n\nJan name: %s\nJan age: %d", jan.name, jan.age);
    return 0;
}