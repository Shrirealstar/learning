#include <stdio.h>
#include <stdlib.h>

#define MAX 100

int stack[MAX];
int top = -1;

void push(int);
int pop();
void display();
void stackStatus();

int main() {
    int choice, element;

    while (1) {
        printf("\n---- Stack Menu ----\n");
        printf("1. Push Element\n");
        printf("2. Pop Element\n");
        printf("3. Display Stack\n");
        printf("4. Display Stack Status\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter element to push: ");
                scanf("%d", &element);
                push(element);
                break;
            case 2:
                element = pop();
                if (element != -1)
                    printf("Popped element: %d\n", element);
                break;
            case 3:
                display();
                break;
            case 4:
                stackStatus();
                break;
            case 5:
                printf("Exiting...\n");
                exit(0);
            default:
                printf("Invalid choice!\n");
        }
    }

    return 0;
}

void push(int element) {
    if (top == MAX - 1) {
        printf("Stack Overflow!\n");
        return;
    }
    stack[++top] = element;
}

int pop() {
    if (top == -1) {
        printf("Stack Underflow!\n");
        return -1;
    }
    return stack[top--];
}

void display() {
    if (top == -1) {
        printf("Stack is empty!\n");
        return;
    }
    printf("Elements in the stack:\n");
    for (int i = top; i >= 0; i--)
        printf("%d\n", stack[i]);
}

void stackStatus() {
    if (top == -1)
        printf("Stack is empty.\n");
    else if (top == MAX - 1)
        printf("Stack is full.\n");
    else
        printf("Stack is neither full nor empty.\n");
}
