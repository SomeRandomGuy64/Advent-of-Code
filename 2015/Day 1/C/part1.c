#include <stdio.h>

int main(void) {
    FILE* ptr;
    char ch;
    int floor = 0;

    ptr = fopen("../instructions.txt", "r");

    if (NULL == ptr) {
        printf("file can't be opened \n");
    }

    do {
        ch = fgetc(ptr);

        if (ch == '(') {
            floor++;
        } else if (ch == ')') {
            floor--;
        }
        

    } while (ch != EOF);

    printf("%d\n", floor);
    fclose(ptr);
    return 0;
}