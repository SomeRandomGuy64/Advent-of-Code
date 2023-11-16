#include <stdio.h>

int main(void) {
    FILE* ptr;
    char ch;
    int floor = 0;
    int position = 0;

    ptr = fopen("instructions.txt", "r");

    if (NULL == ptr) {
        printf("file can't be opened \n");
    }

    do {
        position++;

        ch = fgetc(ptr);

        if (ch == '(') {
            floor++;
        } else if (ch == ')') {
            floor--;
        }

        if (floor == -1) {
            break;
        }
        

    } while (ch != EOF);

    printf("%d\n", position);
    fclose(ptr);
    return 0;
}