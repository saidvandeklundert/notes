#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

// A node of a linked list
struct node {
    int value;
    struct node* next;
};

typedef struct node node;

// print all nodes following a LinkedList head:
void printlist(node *head) {
    node *temp_node = head;
    
    while (temp_node != NULL) {
        printf("%d -> ", temp_node->value);
        temp_node = temp_node->next;
    }
    printf("\n");
}

// Create a new node with a value and a 'next' set to NULL:
node *create_new_node(int value){
    node *result = malloc(sizeof(node));
    result->value = value;
    result->next = NULL;
    return result;
}

// Returns the lenght of the LinkedList:
int get_ll_length(node *head){
    int count = 0;
    node *current = head;
    
    while (current!=NULL){
        count++;
        current = current->next;
    }
    return count;
}

// Verify if an item is present in the LinkedList:
bool contains_value(int value, node *head){
    node *current = head;

    while (current!=NULL){
        if (current->value == value){
            return true;
        } else{
            current = current->next;
        }
    }
    return false;
}


int main(){
    node n1, n2, n3, n4;
    node *head;
    node *tmp_node;
    int ll_length;

    // setting the node values:
    n1.value = 1;
    n2.value = 2;
    n3.value = 3;
    n4.value = 4;

    // linking the nodes together:
    head = &n1;
    n1.next = &n2;
    n2.next = &n3;
    n3.next = &n4;
    n4.next = NULL;
    
    printlist(head);
    ll_length = get_ll_length(head);
    printf("The lenght of the linked list is now %d\n", ll_length );

    node *n5 = create_new_node(5);
    n4.next = n5;

    printlist(head);
    ll_length = get_ll_length(head);
    printf("The lenght of the linked list is now %d\n", ll_length );
    printf("Does the linked list contain 77?\n%d\n", contains_value(77, head) );
    printf("Does the linked list contain 5?\n%d\n", contains_value(5, head) );
    return 0;
}