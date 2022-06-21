#include <stdio.h>
#include <stdlib.h>


// Heap allocated array:
typedef struct vector {
    int len;
    int array[];
} vector;


//Function to create a vector on the heap:
vector *create_vector(size_t vector_size){
    vector *ptr = (vector *)malloc(sizeof(vector *) + vector_size * sizeof(int));
    ptr->len = vector_size;
    return ptr;
}

//Function to copy a vector on the heap:
vector *copy_vector(vector *v){
    // allocate memory for the copy:
    vector *new_vec = (vector *)malloc(sizeof(vector *) + v->len * sizeof(int));
    new_vec->len = v->len;
    // copy the array values from the vector into the copy:
    int i = 0;
    while (i < v->len){
        new_vec->array[i]=v->array[i];
        i++;        
    }    

    return new_vec;
}


// Zeroise a vector:
void zeroize_vector(vector *v){
    int i = 0;
    while (i < v->len){
        v->array[i]=0;
        i++;        
    }
}

// Display the elements inside the vector:
void print_vector(vector *v){
    int i =0;
    while (i <v->len){
        printf("%d\n", v->array[i]);
        i++;             
    }
}

// Free the vector
void free_vector(vector *v) {
  free(v);
  v=NULL;
}

int main() {
    int n;
    n = 10;
    // Initialize a vector:
    vector *ptr = (vector *)malloc(sizeof(vector *) + n * sizeof(int));
    
    // Zeroise the vector:
    for (int i = 0; i < n; i++)
        ptr->array[i]=0;

    printf("The heap allocated array contains the following:\n");
    for (int i = 0; i < n; i++)
        printf("  %d\n", ptr->array[i]);
    printf("\n");
    // free the memory of the vector:
    free(ptr);

    // Create a vector:
    vector *vec = create_vector(20);
    // Populate the vector:
    for (int i = 0; i < vec->len; i++)
        vec->array[i]=1;
    printf("The heap allocated vector 'vec' is of size %d and contains the following:\n", vec->len);
    for (int i = 0; i < vec->len; i++)
        printf("  %d\n", vec->array[i]);
    printf("\n"); 
    zeroize_vector(vec);  
    printf("After zeroizing:\n");
    print_vector(vec);
    printf("\n");
    printf("Made a copy of the vector, the copy contains:\n");
    vector *v_copy;
    v_copy = copy_vector(vec);
    print_vector(vec);

    return 0;
}
