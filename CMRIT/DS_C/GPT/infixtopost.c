#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_SIZE 100

// Function to determine precedence of operators
int precedence(char op) {
    if (op == '^')
        return 3;
    else if (op == '*' || op == '/' || op == '%')
        return 2;
    else if (op == '+' || op == '-')
        return 1;
    else
        return -1;
}

// Function to convert infix expression to postfix expression
void infixToPostfix(char infix[], char postfix[]) {
    char stack[MAX_SIZE];
    int top = -1;
    int i, j;

    for (i = 0, j = 0; infix[i] != '\0'; i++) {
        if (isalnum(infix[i])) {
            postfix[j++] = infix[i];
        } else if (infix[i] == '(') {
            stack[++top] = infix[i];
        } else if (infix[i] == ')') {
            while (top != -1 && stack[top] != '(') {
                postfix[j++] = stack[top--];
            }
            if (top == -1) {
                printf("Invalid expression\n");
                exit(1);
            }
            top--; // Discard '(' from stack
        } else {
            while (top != -1 && precedence(infix[i]) <= precedence(stack[top])) {
                postfix[j++] = stack[top--];
            }
            stack[++top] = infix[i];
        }
    }

    while (top != -1) {
        if (stack[top] == '(') {
            printf("Invalid expression\n");
            exit(1);
        }
        postfix[j++] = stack[top--];
    }

    postfix[j] = '\0';
}

int main() {
    char infix[MAX_SIZE], postfix[MAX_SIZE];

    printf("Enter the infix expression: ");
    fgets(infix, MAX_SIZE, stdin);
    infix[strlen(infix) - 1] = '\0'; // Remove newline character

    infixToPostfix(infix, postfix);
    printf("Postfix expression: %s\n", postfix);

    return 0;
}
