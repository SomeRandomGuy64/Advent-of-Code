# The elves now need to get ribbon for each present
# The length of each ribbon needed is the shortest perimeter of any one face e.g. 2x3x4 has the shortest perimeter of 2+2+3+3 = 10
# The bow fo the ribbon is equal in length to the volume of th present e.g. 2x3x4 needs ribbon of 2*3*4 length

# Read the order_list.txt file and store the contents in a string named ribbon_to_order
# split the contents into a list so that each line of the file (each present) is an item within the list
# initialize an integer named total_ribbon_needed at 0 which represents the total amount of ribbon needed
# loop through the list and for each item in the list find the specific dimensions and store them in their respective integer variables
# e.g. if an item in the list is 2x3x4 then store 2 in an integer variable name length, store 3 in one called width and store 4 in one called height
# when i have all the dimensions of a given item I find the smallest 2 items and add them together before doubling it to find the smallest perimeter, I store this in an integer called smallest_perimeter
# i then multiply each of the dimensions with each other and store the value in a variable called bow length
# i then add smallest_permiter and bow_length and that value to total_ribbon_needed
# once the list has been completely looped through i output total_ribbon_needed
import re

order_list_file = open("../order_list.txt", "r")
ribbon_to_order = order_list_file.read()
dimensions_list = ribbon_to_order.split("\n")

total_ribbon_needed = 0

for dimensions in dimensions_list:
    length = int((re.findall("(\d+)x\d+x\d+", dimensions))[0])
    smallest = length
    second_smallest = length

    width = int((re.findall("\d+x(\d+)x\d+", dimensions))[0])
    if width < smallest:
        smallest = width
    else:
        second_smallest = width

    height = int((re.findall("\d+x\d+x(\d+)", dimensions))[0])
    if height < smallest:
        second_smallest = smallest
        smallest = height
    elif height < second_smallest:
        second_smallest = height

    smallest_perimeter = 2 * (smallest + second_smallest)
    bow_length = length * width * height

    total_ribbon_needed = total_ribbon_needed + smallest_perimeter + bow_length

print(total_ribbon_needed)