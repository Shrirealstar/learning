#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Merge two subarrays of arr[]
// First subarray is arr[l..m]
// Second subarray is arr[m+1..r]
void merge(int arr[], int l, int m, int r) {
    int i, j, k;
    int n1 = m - l + 1;
    int n2 = r - m;

    // Create temporary arrays
    int L[n1], R[n2];

    // Copy data to temporary arrays L[] and R[]
    for (i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];

    // Merge the temporary arrays back into arr[l..r]
    i = 0;
    j = 0;
    k = l;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    // Copy the remaining elements of L[], if any
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    // Copy the remaining elements of R[], if any
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

// l is for left index and r is right index of the sub-array of arr to be sorted
void mergeSort(int arr[], int l, int r) {
    if (l < r) {
        // Same as (l+r)/2, but avoids overflow for large l and r
        int m = l + (r - l) / 2;

        // Sort first and second halves
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);

        // Merge the sorted halves
        merge(arr, l, m, r);
    }
}

void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j < n-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                // Swap arr[j] and arr[j+1]
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

int main() {
    int n;
    printf("Enter the number of elements: ");
    scanf("%d", &n);

    int arr[n], arr_copy[n];
    srand(time(NULL)); // Seed for random number generation

    // Generating random elements
    for (int i = 0; i < n; i++) {
        arr[i] = rand() % 1000; // Adjust range as needed
        arr_copy[i] = arr[i]; // Copy array for bubble sort
    }

    printf("Array before sorting:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    clock_t start = clock();
    mergeSort(arr, 0, n - 1);
    clock_t end = clock();
    
    double merge_sort_time = ((double)(end - start)) / CLOCKS_PER_SEC;

    printf("Array after merge sorting:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    printf("Merge sort time taken: %f seconds\n", merge_sort_time);

    start = clock();
    bubbleSort(arr_copy, n);
    end = clock();
    
    double bubble_sort_time = ((double)(end - start)) / CLOCKS_PER_SEC;

    printf("Array after bubble sorting:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr_copy[i]);
    }
    printf("\n");

    printf("Bubble sort time taken: %f seconds\n", bubble_sort_time);

    return 0;
}
