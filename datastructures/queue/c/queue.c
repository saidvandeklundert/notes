#include <stdio.h>
#include <limits.h>
#include <stdbool.h>
#include <stdlib.h>

#define QUEUE_EMPTY INT_MIN

typedef struct {
    int *values;  // heap-allocated array
    int head, tail, num_entries, size;    
} queue;

void init_queue(queue *q, int max_size){
    q->size  = max_size;
    q->values = malloc(sizeof(int) * q->size);
    q->num_entries = 0;
    q->head = 0;
    q->tail = 0;
}

void q_destroy(queue *q){
    free(q->values);
    free(q);
}

bool queue_empty(queue* q){
    return (q->num_entries ==0);
}

bool queue_full(queue* q){
    return (q->num_entries == q->size);
}

bool enqueue(queue* q, int value){
    if (queue_full(q)){
        return false;
    }
    q->values[q->tail] = value;
    q->num_entries++; // increment the number of items in the queuw
    q->tail = (q->tail +1) % q->size ; // wrap around back to 0
    return true;
}

int dequeue(queue* q){
    int result;

    if (queue_empty(q)) {
        return QUEUE_EMPTY;
    }
    
    result = q->values[q->head];
    q->head = (q->head +1) % q->size;
    q->num_entries--;

    return result;
}

int main(){
    queue q;
    init_queue(&q,10);
    printf("q size %d\nq entries %d\nq tail %d\n", q.size,q.num_entries, q.tail);      
    enqueue(&q, 5);
    printf("q size %d\nq entries %d\nq tail %d\n", q.size,q.num_entries, q.tail);        
    enqueue(&q, 8);
    printf("q size %d\nq entries %d\nq tail %d\n", q.size,q.num_entries, q.tail);      

    enqueue(&q, 1);
    enqueue(&q, 2);
    enqueue(&q, 3);
    enqueue(&q, 4);            
 


    int temp;
    temp = dequeue(&q);
    printf("dequeue temp %d\n\n\n\n", temp);
    printf("q size %d\nq entries %d\nq tail %d\n", q.size,q.num_entries, q.tail);  
    while ((temp = dequeue(&q)) != QUEUE_EMPTY) {
        printf("temp %d\n", temp);
    }
    
      
}