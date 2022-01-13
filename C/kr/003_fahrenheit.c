#include <stdio.h>

main()
{
    float fahr, celsius;
    int lower, upper, step;

    lower = 0;
    upper = 300;
    step = 20;

    fahr = lower;
    printf("Celsius\t| Fahrenheit\n________________\n", fahr, celsius);
    while (fahr <= upper)
    {
        celsius = (5.0 / 9.0) * (fahr - 32.0);

        printf("%3.0f\t| %6.1f\n", fahr, celsius);
        fahr = fahr + step;
    }
}