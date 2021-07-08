#include <stdio.h>

void flush_input()
{
    int ch;
    while ((ch = getchar()) != '\n' && ch != EOF)
        ;
}

void getinput_with_gets()
{
    char firstname[5];
    char lastname[5];
    printf("Enter your first name:");
    gets(firstname);
    printf("Enter your last name:");
    gets(lastname);
    printf("Hello, %s, %s\n", firstname, lastname);
}

void getinput_with_fgets()
{
    char firstname[5];
    char lastname[5];
    printf("Enter your first name:");
    fgets(firstname, 5, stdin);
    printf("Enter your last name:");
    // fflush(stdin);	// This function may not (invariably) work with input!
    flush_input();
    fgets(lastname, 5, stdin);
    flush_input();
    printf("Hello, %s, %s\n", firstname, lastname);
}

int main(int argc, char **argv)
{
    // getinput_with_gets();
    getinput_with_fgets();
    return 0;
}