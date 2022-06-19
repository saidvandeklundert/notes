#include <stdio.h>

int main()
{
    // Basic array:
    double array[4];
    array[0] = 0.0;
    array[1] = 1.0;
    array[2] = 2.0;
    array[3] = 3.0;
    printf("%f\n", array[0]);

    // Looping through an array can be done as follows:
    //  1. determine the length of the array
    //  2. use a while loop to step through the array

    // Get the size of the array and the individual element in it
    // Then calculate the length
    int array_length = sizeof(array) / sizeof(array[0]);
    printf("The array contains %d elements.\n", array_length);
    
    int i;
    i = 0;
    while (i < array_length){        
        printf("Array element %d is %f.\n", i, array[i]);
        i++;
    }
    



    /*
    double two_dimensional_array[2][2];

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
    */
    return 0;
}