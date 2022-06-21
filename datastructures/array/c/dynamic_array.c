/*
TODO: shrink to fit

TODO: erase elements

TODO: remote last element

TODO: add element to the end
*/
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#define INITIAL_VECTOR_CAPACITY 64

// Heap allocated dynamic array:
typedef struct vector {    
    int* array;
    int size;
    int capacity;    
} vector;


//Function to create a vector on the heap:
vector *create_vector(size_t vector_size){
    vector *v_ptr = (vector *)malloc(sizeof(vector *) + vector_size * sizeof(int));
    if (v_ptr == NULL){
        fprintf(stderr, "Not enough memory.");
        abort();
    }
    v_ptr->size = vector_size;
    v_ptr->capacity = INITIAL_VECTOR_CAPACITY;
    v_ptr->array = (int*) malloc( sizeof(int)* v_ptr->capacity);
    if (v_ptr->array == NULL){
        fprintf(stderr, "Not enough memory.");
        abort();
    }    
    return v_ptr;
}

// Free the vector's memory:
void vector_destroy(vector *v){
    assert(v);
    free(v->array);
    free(v);
}

//Double capacity
void vector_double_capacity(vector *v){
    assert(v);
    // determine new capacity:
    int new_capacity = 2 * v->capacity;
    // allocate memory for the new capacity
    int* new_array = (int*) malloc(sizeof(int)*new_capacity);
    if (new_array == NULL) {
        fprintf(stderr, "Not enough memory!");
        abort();
    }
    // copy over the content from the old array to the new array
    for(int i = 0; i < v->size; i++) {
        new_array[i] = v->array[i];
    }
    // free the old array:
    free(v->array);
    // set the pointer from the old to the new array and update the capacity:
    v->array = new_array;
    v->capacity = new_capacity;
}    

//Half the capacity of the vector:
void vector_half_capacity(vector *v){
    assert(v);
    if (v->capacity <= INITIAL_VECTOR_CAPACITY){
        return;
    }

    int new_capacity = v->capacity /2;
    int* new_array = (int*) malloc(sizeof(int)*new_capacity);

    if (new_array==NULL){
        fprintf(stderr, "Not enough memory.");
        abort();
    }

    for(int i = 0; i < min(v->size, new_capacity); i++){
        new_array[i] = v->array[i];
    }

    free(v->array);
    v->array = new_array;
    v->capacity = new_capacity;
    v->size = min(v->size, new_capacity);

}

// Print all the elements in the vector:
void vector_printer(vector *v){
    for (int i = 0; i < v->size; i++)
        printf("  %d\n", v->array[i]);
    printf("\n");    
}

// Add an element to the vector:
void vector_add(vector *v, int element){
    assert(v);

    // If the backing array nears capacity, double it:
    if (v->size >= v->capacity){
        vector_double_capacity(v);
    }
    // add the element at the end and increment the
    // size of the vector:
    v->array[v->size++] = element;
}

// Get an element from the vector:
int vector_get(vector *v, int i){
    assert(v);
    if (i<0 || i >= v->size){
        fprintf(stderr, "Out of index.");
        abort();
    }
    return v->array[i];
}

// Place an element somewhere in the vector:
void vector_put(vector *v, int index, int value){
    assert(v);
    if (index <0 || index >= v->size) {
        fprintf(stderr, "Out of index");
        abort();
    }
    v->array[index] = value;
}

// Add an alement to the vector and shift all existing elements:
void vector_add_and_shift(vector *v, int index, int element){
    assert(v);

    if (index < 0 || index >= v->size){
        fprintf(stderr, "Out of index");
        abort();        
    }

    if (v->size >= v->capacity){
        vector_double_capacity(v);
    }

    for(int j = v->size; j>index; j--){
        v->array[j] = v->array[j-1];
    }
    v->array[index]= element;
    v->size++;
}



// Check if the vector is empty,
// 1 is true and 0 is false.
int vector_is_empty(vector *v){
    assert(v);
    return v->size == 0;
}

// get the size of the vector:
int vector_size(vector *v){
    assert(v);
    return v->size;
}

// Get the capacity of the vector:
int vector_capacity(vector *v){
    assert(v);
    return v->capacity;
}

// Write all 0's to the vector
void vector_zeroise(vector *v){
    for (int i = 0; i < v->size; i++)
        v->array[i]=0;    
}

// Clears the vector:
void vector_clear(vector *v){
    int new_capacity = INITIAL_VECTOR_CAPACITY;
    int* new_array = (int*) malloc(sizeof(int)*new_capacity);
    if (new_array==NULL){
        fprintf(stderr, "Not enough memory.");
        abort();
    }    
    free(v->array);
    v->array = new_array;
    v->capacity = new_capacity;
    v->size = new_capacity;
    vector_zeroise(v);
}



int main() {
    printf("Start.\n");
    int n;
    n = 5;
    // Initialize a vector:
    vector *v_ptr = create_vector(n);
    
    // Zeroise the vector:
    for (int i = 0; i < n; i++)
        v_ptr->array[i]=0;

    printf("The heap allocated array contains the following:\n");
    vector_printer(v_ptr);

    printf("\ncapacity: %d\n", v_ptr->capacity);
    vector_double_capacity(v_ptr);
    printf("\ncapacity after doubling: %d\n", v_ptr->capacity);
    vector_printer(v_ptr);
    vector_half_capacity(v_ptr);
    printf("\ncapacity after halving: %d\n", v_ptr->capacity);
    vector_printer(v_ptr);
    vector_put(v_ptr, 2, 234);
    printf("After 'vector_put'.\n");
    vector_printer(v_ptr);
    printf("Running 'vector_get(2)': %d\n", vector_get(v_ptr,2));
    vector_add_and_shift(v_ptr,2, 185);
    printf("After 'vector_add_and_shift'.\n");
    vector_printer(v_ptr);    
    vector_clear(v_ptr);
    printf("After 'vector_clear'.\n");
    vector_printer(v_ptr);    
    vector_destroy(v_ptr);
    return 0;
}
