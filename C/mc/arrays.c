#include <stdio.h>

int main()
{
    // Example arrays:
    double array[4];
    double two_dimensional_array[2][2];
    array[0] = 0.0;
    array[1] = 1.0;
    array[2] = 2.0;
    array[3] = 3.0;
    printf("%f\n", array[0]);
    char string_array[3][20] = {
        "Hello",
        "World",
        "!"};
    printf("%s\n", string_array[0]);
    printf("%s\n", string_array[1]);
    printf("%s\n", string_array[2]);
    size_t string_arrayLen = sizeof string_array / sizeof string_array[0];
    printf("array lenght: %d\n", string_arrayLen);
    for (size_t i = 0; i < string_arrayLen; ++i)
    {
        printf("element %s \n",
               string_array[i]);
    }
    int arr[] = {2, 4, 6, 8};
    int arrLen = sizeof arr / sizeof arr[0];

    int i = 0;
    while (i < arrLen)
    {
        printf("%d\n", arr[i]);
        i++;
    }
    return 0;
}