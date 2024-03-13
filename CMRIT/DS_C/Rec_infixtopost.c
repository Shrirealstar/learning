#include<stdio.h>
#define M 20
int top=-1;
char str[M];
char stack[M];
void push(char ch)
{
    top++;
    stack[top]=ch;
}
char pop()
{
    char v = stack[top];
    top--;
    return v;
}
int prec(char op)
{
    switch(op)
    {
        case '^':
            return 3;
        case '*':
        case '/':
        case '%':
            return 2;
        case '+':
        case '-':
            return 1;
        default:
            return 0;
    }
}

void convert()
{
    printf("The postfix exp is: ");
    for(int i=0;str[i]!='\0';i++)
    {
        switch(str[i])
        {
            case '(':
                push(str[i]);
                break;
            case ')':
                while(stack[top]!='(')
                {
                    char y = pop();
                    printf("%c",y);
                }
                if(stack[top]=='(')
                    pop();
                break;
            case '+':
            case '-':
            case '*':
            case '/':
            case '%':
            case '^':
                while(top>=0 && prec(str[i]<=prec(stack[top]))){
                    char x = pop();
                    printf("%c",x);
                }
                push(str[i]);
                break;
            default:
                printf("%c",str[i]);
        }
    }
    while(top>=0)
    {
        char x= pop();
        printf("%c",x);
    }
    printf("\n");
}

void main()
{
    printf("Enter the infix string: ");
    scanf("%s",str);
    convert();
}