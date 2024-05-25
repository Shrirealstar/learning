#include<stdio.h>
void main(){
    int a[5];
    int i;
    while(int i =0; i < 5; i++){
        printf("Enter a[%d] : ",i);
        scanf("%d", &a[i]);
    }
    for(int i =0; i < 5; i++){
        printf("Array of %d is %d:\n ",i,a[i]);
    }
}