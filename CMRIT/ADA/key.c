#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<time.h>

int n;
int key;
int a[20000];
int i;
int found = 0;

int main(){

    printf("Enter the size of the array : ");
    scanf("%d",&n);

    for(i = 0; i<n; i++){
        printf("Enter the elements : ");
        scanf("%d", &a[i]);
    }

    printf("Enter the key : ");
    scanf("%d", &key);

    clock_t start_time = clock(); // Start timing

    for(i = 0; i<n; i++){
        if(a[i] == key){
            printf("Key found at %d position\n", i+1);
            found = 1;
            break;
        }
    }

    if(found == 0){
        printf("Key not found\n");
    }

    clock_t end_time = clock(); // End timing

    double time_taken = ((double)end_time - start_time) / CLOCKS_PER_SEC;
    printf("Execution time: %f seconds\n", time_taken);

    return 0;
}
