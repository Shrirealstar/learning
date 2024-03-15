#include<stdio.h>
#include<stdlib.h>

#define MAX 100

int stack[MAX];
int top = -1;

void push(int);
int pop();
void display();
void status();

int main() {
    int choice;
    int element;

    for (;;) {
        printf("\n----------Menu----------\n");
        printf("1. Push\n");
        printf("2. Pop\n");
        printf("3. Display\n");
        printf("4. Status\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter an element to push: ");
                scanf("%d", &element);
                push(element);
                break;
            case 2:
                element = pop();
                if (element != -1) {
                    printf("Popped element is: %d\n", element);
                }
                break;
            case 3:
                display();
                break;
            case 4:
                status();
                break;
            case 5:
                printf("Exiting...\n");
                exit(0);
                break;
            default:
                printf("\nInvalid choice\n");
        }
    }

    return 0;
}

void push(int element) {
    if (top == MAX - 1) {
        printf("Stack Overflow !!!\n");
        return;
    }
    stack[++top] = element;
}

int pop() {
    if (top == -1) {
        printf("Stack Underflow\n");
        return -1;
    }
    return stack[top--];
}

void display() {
    if (top == -1) {
        printf("Stack is Empty\n");
        return;
    }
    printf("Stack elements are:\n");
    for (int i = top; i >= 0; i--) {
        printf("%d\n", stack[i]);
    }
}

void status() {
    if (top == -1) {
        printf("Stack is Empty\n");
    } else if (top == MAX - 1) {
        printf("Stack is Full\n");
    } else {
        printf("Stack is neither Full nor Empty\n");
    }
}
