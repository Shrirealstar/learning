#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define MAX_EMPLOYEES 100 // Maximum number of employees
#define MAX_HT_SIZE 20 // Maximum size of the hash table

int ht[MAX_HT_SIZE];
int m;

void insert(int x);
void display();

int main(){
    int N, key;
    
    // Prompt user for the number of employee records
    printf("Enter the number of employee records: ");
    scanf("%d", &N);
    
    // Prompt user for the size of the hash table
    printf("Enter the size of the hash table: ");
    scanf("%d", &m);
    
    memset(ht, -1, sizeof(int)*MAX_HT_SIZE);
    
    // Input employee records
    for (int i = 0; i < N; i++) {
        printf("Enter the key for employee record %d: ", i+1);
        scanf("%d", &key);
        insert(key);
    }
    
    // Display the hash table
    display();
    
    return 0;
}

// Hash function: H(K) = K mod m
int hash(int key) {
    return key % m;
}

// Insert employee record into hash table
void insert(int x){
    int index = hash(x);
    
    // Linear probing to resolve collisions
    while (ht[index] != -1) {
        index = (index + 1) % MAX_HT_SIZE;
    }
    
    ht[index] = x;
}

// Display the hash table
void display(){
    printf("Hash Table:\n");
    for(int i = 0; i < MAX_HT_SIZE; i++){
        printf("%d\t", ht[i]);
    }
    printf("\n");
}
