#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define MAX 10
int queue[MAX];

int front = -1;
int rear = -1;

void insertelement(int element);
int deleteelement();
void displayqueue();
int isEmpty();
int isFull();

int main() {
    int choice;
    int element;

    for (;;) {
        printf("\n_____Menu_____\n");
        printf("1. Insert an element\n");
        printf("2. Delete an element\n");
        printf("3. Display the queue\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);
        
        switch (choice) {
            case 1:
                printf("Enter the element to insert: ");
                scanf("%d", &element);
                insertelement(element);
                break;
            case 2:
                element = deleteelement();
                if (element != -1) {
                    printf("Deleted element: %d\n", element);
                }
                break;
            case 3:
                displayqueue();
                break;
            case 4:
                printf("Exiting...\n");
                exit(0);
            default:
                printf("Invalid choice\n");
        }

    }
}

void insertelement(int element) {
    if (isFull()) {
        printf("Queue is full\n");
        return;
    }
    if (front == -1) {
        front = 0;
    }
    rear = (rear + 1) % MAX;
    queue[rear] = element;
}

int deleteelement() {
    if (isEmpty()) {
        printf("Queue is empty\n");
        return;
    }
    int element = queue[front];
    if (front == rear) {
        front = rear = -1;
    } else {
        front = (front + 1) % MAX;
    }
    return element;
}

 void displayqueue() {
    if (isEmpty()) {
        printf("Queue is empty\n");
        return;
    }
    int i;
    printf("Queue: ");
    for (i = front; i != rear; i = (i + 1) % MAX) {
        printf("%d ", queue[i]);
    }
}

int isEmpty() {
    return front == -1;
}

int isFull() {
    return (rear + 1) % MAX == front;
}