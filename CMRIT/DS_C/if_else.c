#include<stdio.h>
int main()
{
    int a;
    printf("Enter a number :\n");
    scanf("%d",&a);

    if( a > 0)
    {
        printf("Positive\n");
    }

    else if( a < 0)
    {
        printf("Negitive\n");
    }
    else 
    {
        printf("Zero\n");
    }


}