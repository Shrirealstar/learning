#include<stdio.h>

struct employ
{
    char name[10];
    int age;
    float salary;
};

void main ()
{
    struct employ a;
    {
        printf("Enter Name : ");
        scanf("%s",a.name);
        printf("Enter Age : ");
        scanf("%d",&a.age);
        printf("Enter Salary : ");
        scanf("%f",&a.salary);

    };

    printf("Name is : %s\n",a.name);
    printf("Age is : %d\n",a.age);
    printf("Salary is : %f\n",a.salary);
}