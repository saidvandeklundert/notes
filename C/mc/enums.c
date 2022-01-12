#include <stdio.h>

enum color
{
    PURPLE,
    WHITE,
    BLACK
};

typedef enum
{
    RED,
    GREEN,
    BLUE
} colors;
int main()
{

    enum color kleur;
    kleur = WHITE;
    printf("WHITE: %d\n", kleur);

    printf("RED: %d\n", RED);
    printf("GREEN: %d\n", GREEN);
    printf("BLUE: %d\n", BLUE);
    return 0;
}