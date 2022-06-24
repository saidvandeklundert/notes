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

// print some tabs
void print_tabs(int number_of_tabs){
    for (int i=0; i<number_of_tabs; i++){
        printf("\t");
    }
}

// Get the height of the binary tree:
int height(treenode *root){
    if (root == NULL){
        return 0;
    } else{
        // Get the heigt from both left and right:
        int right_height = height(root->right);
        int left_height = height(root->left);

        // The final height is the heigt of the greatest subtree (left or right)
        // plus 1 (which is that of the root's level).
        if (right_height > left_height){
            return (right_height +1);
        } else{
            return (left_height+1);
        }
    }
}

// Insert a node into a tree
treenode *insert(treenode *root, int data){
    // if the root is NULL, insert the data here:
    if (root ==NULL) {
        root = create_node(data);
    } else if (data > root->value) {
        // if input value is bigger then the root value, insert the data
        // in the right leaf:
        root->right = insert(root->right, data);
    } else if (data < root->value) {
        // if input value is smaller then the root value, insert the data
        // in the left leaf:        
        root->left = insert(root->left, data);
    }
    // Return the modified tree
    return root;
}


// Free all nodes:
void purge_tree(treenode *root){
    if (root != NULL){
        purge(root->left);
    }
    if (root != NULL){
        purge(root->right);
    }     
    free(root);
    root = NULL;
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
    treenode *root = create_node(1);
    treenode *n2 = create_node(2);
    treenode *n3 = create_node(3);
    treenode *n4 = create_node(4);
    treenode *n5 = create_node(5);
    
    root->left = n2;
    root->right = n3;
    n3->left = n4;
    n3->right = n5;
    print_tree_root(root);
    insert(root,10);
    insert(root,13);
    insert(root,2324);
    insert(root,6);
    print_tree_root(root);
    int tree_height = height(root);
    printf("Tree height is : %d", tree_height);
    purge_tree(root);
    
    return 1;
}