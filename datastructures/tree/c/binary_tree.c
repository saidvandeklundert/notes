#include <stdio.h>
#include <stdlib.h>


typedef struct treenode {
    int value;
    struct treenode *left;
    struct treenode *right;

} treenode;

treenode *create_node(int value){
    treenode* result = malloc(sizeof(treenode));
    if (result !=NULL){
        result->left = NULL;
        result->right = NULL;
        result->value=value;
        
    } else{
        fprintf(stderr, "Could not create treenode.");
        abort();
    }
    return result;
}


void print_tabs(int number_of_tabs){
    for (int i=0; i<number_of_tabs; i++){
        printf("\t");
    }
}

// print the tree to screen in pre-order traversal:
void print_tree_rec(treenode *node, int level){
    if (node == NULL){
        print_tabs(level);
        printf("-- emptry tree --\n");
        return;
    }
    print_tabs(level);
    printf("value : %d\n", node->value);
    print_tabs((level +1));
    printf("left--\n");
    print_tree_rec(node->left, (level +2));
    print_tabs((level +1));
    printf("right--\n");
    print_tree_rec(node->right, (level +2));

}

// print the root tree
void print_tree_root(treenode *root){
    print_tree_rec(root, 1);
}

int main(){
    treenode *n1 = create_node(1);
    treenode *n2 = create_node(2);
    treenode *n3 = create_node(3);
    treenode *n4 = create_node(4);
    treenode *n5 = create_node(5);
    
    n1->left = n2;
    n1->right = n3;
    n3->left = n4;
    n3->right = n5;
    print_tree_root(n1);
    free(n1);
    free(n2);
    free(n3);
    free(n4);
    free(n5);
    return 1;
}