#include<stdio.h>
#include<stdlib.h>
#include<string.h>

struct day {
    char *name;
    int date;
    char *display;
};


void create(struct day *calender);
void read(struct day *calender);
void display(struct day *calender);

int main() {

    struct day *calender = malloc(20 *sizeof(calender));

    create(calender);
    read(calender);
    display(calender);
}


//Create
void create(struct day *calender){
    for(int i=0;i<7;i++){
        calender[i].name = malloc(20*sizeof(char));
        calender[i].display = malloc(20*sizeof(char));
    }
}

//Read
void read(struct day *calender){
    for(int i=0;i<7;i++){
        printf("Enter the name of the day: ");
        scanf("%s",calender[i].name);
        printf("Enter the date: ");
        scanf("%d",&calender[i].date);
        printf("Enter the Activity: ");
        scanf("%s",calender[i].display);
    }
}

//Display
void display(struct day *calender){
    printf("Name\tDate\tActivity\n");
    printf("--------------------------------------------------\n");
    for(int i=0;i<7;i++){
        printf("%s\t%d\t%s\n", calender[i].name, calender[i].date, calender[i].display);
    }
}