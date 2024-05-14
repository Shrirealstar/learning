#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Function to swap two integers
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Function to perform selection sort
void selectionSort(int arr[], int n) {
    int i, j, min_index;
    for (i = 0; i < n-1; i++) {
        min_index = i;
        for (j = i+1; j < n; j++) {
            if (arr[j] < arr[min_index])
                min_index = j;
        }
        swap(&arr[min_index], &arr[i]);
    }
}

int main() {
    int n, i;
    clock_t start, end;
    double cpu_time_used;

    printf("Enter the number of elements: ");
    scanf("%d", &n);

    int *arr = (int*)malloc(n * sizeof(int));

    // Generate random numbers
    srand(time(0));
    for (i = 0; i < n; i++) {
        arr[i] = rand() % 1000;  // Random integers between 0 and 999
    }

    // Display the unsorted array
    printf("Unsorted Array: ");
    for (i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    // Record the start time
    start = clock();

    // Perform selection sort
    selectionSort(arr, n);

    // Record the end time
    end = clock();

    // Display the sorted array
    printf("Sorted Array: ");
    for (i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    // Calculate the CPU time used
    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
    printf("Time taken for execution: %f seconds\n", cpu_time_used);

    // Free dynamically allocated memory
    free(arr);

    return 0;
}
