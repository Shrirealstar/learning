#include <stdio.h>

// Function to swap two numbers using pointers
void swapNumbers(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main() {
    int num1 = 5, num2 = 10;

    printf("Before swapping: num1 = %d, num2 = %d\n", num1, num2);

    // Pass the addresses of num1 and num2 to the swapNumbers function
    swapNumbers(&num1, &num2);

    printf("After swapping: num1 = %d, num2 = %d\n", num1, num2);

    return 0;
}
