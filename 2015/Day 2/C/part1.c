#include <stdio.h>

#define LINE_LENGTH 10
#define DIMENSION_ARRAY_SIZE 2
#define EMPTY_VALUE 'n'

int double_areas_of_side(int length_one, int length_two) {
    return length_one * length_two * 2;
}

int find_smallest_area(int length_one, int length_two, int length_three) {
    int smallest = length_one;
    int second_smallest = length_one;

    if (length_two < smallest) {
        smallest = length_two;
    } else {
        second_smallest = length_two;
    }

    if (length_three < smallest) {
        second_smallest = smallest;
        smallest = length_three;
    } else if (length_three < second_smallest) {
        second_smallest = length_three;
    }

    return smallest * second_smallest;
}

int convert_char_array_to_int(char *dimension_array, int size) {
    int dimension = 0;

    if (dimension_array[1] == EMPTY_VALUE) {
        dimension = dimension_array[0] - '0';
    } else {
        for (int i = 0; i < size; i++) {
            dimension = dimension * 10 + (dimension_array[i] - '0');
        }
    }

    
    return dimension;
}

int main(void) {
    FILE* ptr;
    char str[LINE_LENGTH];
    int total_paper_needed = 0;

    ptr = fopen("../order_list.txt", "r");

    if (ptr == NULL) {
        printf("file can't be opened \n");
    }

    while (fgets(str, LINE_LENGTH, ptr) != NULL) {
        char length_array[DIMENSION_ARRAY_SIZE] = {EMPTY_VALUE, EMPTY_VALUE};
        char width_array[DIMENSION_ARRAY_SIZE] = {EMPTY_VALUE, EMPTY_VALUE};
        char height_array[DIMENSION_ARRAY_SIZE] = {EMPTY_VALUE, EMPTY_VALUE};
        int check_position = 0;
        int array_position = 0;

        for (int i = 0; i < sizeof(str) / sizeof(str[0]); i++) {

            if (str[i] == 'x') {
                check_position++;
                array_position = 0;
                continue;
            } else if (str[i] == '\n' || str[i] == '\0') {
                break;
            }

            switch (check_position) {
            case 0:
                length_array[array_position] = str[i];
                array_position++;
                break;

            case 1:
                width_array[array_position] = str[i];
                array_position++;
                break;

            case 2:
                height_array[array_position] = str[i];
                array_position++;
                break;
            
            default:
                break;
            }
        }

        //combining char arrays into ints
        int length = convert_char_array_to_int(length_array, DIMENSION_ARRAY_SIZE);
        int width = convert_char_array_to_int(width_array, DIMENSION_ARRAY_SIZE);
        int height = convert_char_array_to_int(height_array, DIMENSION_ARRAY_SIZE);

        int two_l_w = double_areas_of_side(length, width);
        int two_w_h = double_areas_of_side(width, height);
        int two_h_l = double_areas_of_side(height, length);
        int smallest_area = find_smallest_area(length, width, height);

        int total_paper_for_present = two_h_l + two_l_w + two_w_h + smallest_area;

        total_paper_needed += total_paper_for_present;
    }

    fclose(ptr);

    printf("%d\n", total_paper_needed);
    return 0;
}