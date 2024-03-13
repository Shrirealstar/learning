#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_DESCRIPTION_LENGTH 100

// Define the structure for a day
struct Day {
    char *name;
    int date;
    char *description;
};

// Function prototypes
void create(struct Day *calendar);
void read(struct Day *calendar);
void display(struct Day *calendar);

int main() {
    // Allocate memory for 7 days
    struct Day *calendar = (struct Day *)malloc(7 * sizeof(struct Day));

    create(calendar);
    read(calendar);
    display(calendar);

}

// Function to create the calendar
void create(struct Day *calendar) {
    char dayNames[7][10] = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"};

    for (int i = 0; i < 7; i++) {
        calendar[i].name = (char *)malloc(strlen(dayNames[i]) + 1);
        strcpy(calendar[i].name, dayNames[i]);
        calendar[i].date = 0;
        calendar[i].description = (char *)malloc(MAX_DESCRIPTION_LENGTH + 1);
    }
}

// Function to read data from the keyboard
void read(struct Day *calendar) {
    for (int i = 0; i < 7; i++) {
        printf("Enter date for %s: ", calendar[i].name);
        scanf("%d", &calendar[i].date);
        getchar(); // Clear the newline character from the input buffer
        
        printf("Enter activity description for %s: ", calendar[i].name);
        fgets(calendar[i].description, MAX_DESCRIPTION_LENGTH, stdin);
        calendar[i].description[strcspn(calendar[i].description, "\n")] = '\0'; // Remove newline character if present
    }
}

// Function to display the calendar
void display(struct Day *calendar) {
    printf("\nCalendar:\n");
    for (int i = 0; i < 7; i++) {
        printf("Day: %s\n", calendar[i].name);
        printf("Date: %d\n", calendar[i].date);
        printf("Activity: %s\n", calendar[i].description);
        printf("\n");
    }
}
