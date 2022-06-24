/*
    Compilation process:
    - character mapping
    - line splicing
    - tokenization
    - preprocessing                 <---- !! here
    - character-set mapping
    - string concatenation
    - translation
    - linkage

    Preprocessor runs before the source code is translated into object code.

    Preprocssing directives are called as follows:
    #<directive>

    Example:
    #include <stdio.h>
    #define
    #if

    You can look at the preprocessor output:
        clang other-options -E -o output_file.i source.c
        gcc other-options -E -o output_file.i source.c
        cl other-options /P /Fi output_file source.c

    To see the output for this file:

        cl /P /C pre_processor.c

        Then ctrl+f 'int main(){'
*/
#include <stdio.h>

#define NUMBER 100

int main(){
    int i;
    i = NUMBER;
    printf("NUMBER is :%d", i);
    //printf("\ncapacity after doubling: %d\n", v_ptr->capacity);
    return 1;
}