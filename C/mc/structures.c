#include <stdio.h>

// Forward-declared the struct within a typedef using the same identifier as the tag name.
typedef struct Person Person;
struct Person
{
    char name[25];
    int age;
};

typedef struct Human
{
    char name[25];
    int age;
} Human;

int main()
{

    Human jan = {.name = "Jan", .age = 123};
    printf("%s\n", jan.name);
    Person marie = {.name = "Marie", .age = 123};
    printf("%s\n", marie.name);
    return 0;
}