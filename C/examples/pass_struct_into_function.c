#include <stdio.h>
#include <string.h>

struct human {
    char name[20];
    int age;
};

typedef struct human human;

// Following function takes a copy of the human struct:
void increase_age_pass_by_value(human human){
    human.age = human.age ++;
    printf("inside 'increase_age_pass_by_value', human is now %d years old.\n", human.age);
}

// Following function takes a reference of the human struct:
void increase_age_pass_by_reference(human *human){
    human->age = human->age ++;
    printf("inside 'increase_age_pass_by_reference', human is now %d years old.\n", human->age);
}




int main(){
    human human_1;
    human_1.age=6; 
    strcpy(human_1.name, "Jan");

    increase_age_pass_by_value(human_1);
    printf("After running 'increase_age_pass_by_value', human is %d years old.\n", human_1.age);    
    increase_age_pass_by_reference(&human_1);
    printf("After running 'increase_age_pass_by_reference', human is %d years old.\n", human_1.age);    
    
    return 0;
}