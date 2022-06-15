#include <stdio.h>
#include <limits.h>
#include <stdbool.h>

#define STACK_LENGTH 10
#define EMPTY (-1)
#define STACK_EMPTY INT_MIN

int stack[STACK_LENGTH];

int top = EMPTY;

bool push(int value){
    if (top>=STACK_LENGTH-1) return false;

    top++;
    stack[top]=value;
    return true;
}

int pop(){
    if (top == EMPTY) return STACK_EMPTY;
    int result = stack[top];
    top--;
    return result;
}

int main(){
    push(1);
    push(2);
    push(3);
    int temp;
    while ((temp = pop()) != STACK_EMPTY){
        printf("temp = %d\n", temp);
    }
}