#include <stdio.h>

enum week
{
    Mon,
    Tue,
    Wed,
    Thur,
    Fri,
    Sat,
    Sun
};

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
    enum week day;
    day = Wed;
    printf("%d", day);

    enum color kleur;
    kleur = WHITE;
    printf("%d", kleur);
    return 0;
}