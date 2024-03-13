#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *left;
    struct node *right;
};

// Function prototypes
struct node *createNode(int data);
struct node *insert(struct node *root, int data);
struct node *search(struct node *root, int key);
void inorderTraversal(struct node *root);
void preorderTraversal(struct node *root);
void postorderTraversal(struct node *root);


int main() {
    struct node *root = NULL;
    int choice, key;
    
    // Creating the BST
    int elements[] = {6, 9, 5, 2, 8, 15, 24, 14, 7, 8, 5, 2};
    int num_elements = sizeof(elements) / sizeof(elements[0]);
    for (int i = 0; i < num_elements; i++) {
        root = insert(root, elements[i]);
    }
    
    do {
        printf("\n----- Menu -----\n");
        printf("1. Traverse BST in Inorder\n");
        printf("2. Traverse BST in Preorder\n");
        printf("3. Traverse BST in Postorder\n");
        printf("4. Search element in BST\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);
        
        switch (choice) {
            case 1:
                printf("Inorder Traversal: ");
                inorderTraversal(root);
                printf("\n");
                break;
            case 2:
                printf("Preorder Traversal: ");
                preorderTraversal(root);
                printf("\n");
                break;
            case 3:
                printf("Postorder Traversal: ");
                postorderTraversal(root);
                printf("\n");
                break;
            case 4:
                printf("Enter the element to search: ");
                scanf("%d", &key);
                if (search(root, key) != NULL)
                    printf("%d is found in the BST.\n", key);
                else
                    printf("%d is not found in the BST.\n", key);
                break;
            case 5:
                printf("Exiting program...\n");
                break;
            default:
                printf("Invalid choice! Please enter a valid option.\n");
        }
    } while (choice != 5);

    return 0;
}

// Function to create a new node
struct node *createNode(int data) {
    struct node *newNode = (struct node *)malloc(sizeof(struct node));
    newNode->data = data;
    newNode->left = newNode->right = NULL;
    return newNode;
}

// Function to insert a node in the BST
struct node *insert(struct node *root, int data) {
    if (root == NULL)
        return createNode(data);
    if (data < root->data)
        root->left = insert(root->left, data);
    else if (data > root->data)
        root->right = insert(root->right, data);
    return root;
}

// Function to search for a key in the BST
struct node *search(struct node *root, int key) {
    if (root == NULL || root->data == key)
        return root;
    if (root->data < key)
        return search(root->right, key);
    return search(root->left, key);
}


// Function to perform inorder traversal
void inorderTraversal(struct node *root) {
    if (root != NULL) {
        inorderTraversal(root->left);
        printf("%d ", root->data);
        inorderTraversal(root->right);
    }
}

// Function to perform preorder traversal
void preorderTraversal(struct node *root) {
    if (root != NULL) {
        printf("%d ", root->data);
        preorderTraversal(root->left);
        preorderTraversal(root->right);
    }
}

// Function to perform postorder traversal
void postorderTraversal(struct node *root) {
    if (root != NULL) {
        postorderTraversal(root->left);
        postorderTraversal(root->right);
        printf("%d ", root->data);
    }
}

