#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void merge(int arr[], int l, int m, int r) {
    int n1 = m - l + 1;
    int n2 = r - m;
    int L[n1], R[n2];

    for (int i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (int j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];

    int i = 0, j = 0, k = l;
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

    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

void mergeSort(int arr[], int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);
        merge(arr, l, m, r);
    }
}

void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

void printArray(int arr[], int n) {
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

int main() {
    int n;
    printf("Enter the number of elements: ");
    scanf("%d", &n);

    int arr[n], arr_copy[n];
    srand(time(NULL));

    for (int i = 0; i < n; i++) {
        arr[i] = rand() % 1000;
        arr_copy[i] = arr[i];
    }

    printf("Array before sorting:\n");
    printArray(arr, n);

    clock_t start = clock();
    mergeSort(arr, 0, n - 1);
    clock_t end = clock();
    double merge_sort_time = ((double)(end - start)) / CLOCKS_PER_SEC;

    printf("Array after merge sorting:\n");
    printArray(arr, n);
    printf("Merge sort time taken: %f seconds\n", merge_sort_time);

    start = clock();
    bubbleSort(arr_copy, n);
    end = clock();
    double bubble_sort_time = ((double)(end - start)) / CLOCKS_PER_SEC;

    printf("Array after bubble sorting:\n");
    printArray(arr_copy, n);
    printf("Bubble sort time taken: %f seconds\n", bubble_sort_time);

    return 0;
}
