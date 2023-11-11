# there is a list of dimensions (lengthxwidthxheight) in the file order_list.txt
# the dimenstions are for the presents which the elves need to wrap, they are all perfect right rectangular prisms
# for each present i must make the calculation 2*length*width + 2*width*height + 2*height*length to calculate the surface area
# i must also add on the area of the smallest side for slack

# Read the file and store the contents in a string named paper_to_order
# split the contents into a list so that each line of the file (each present) is an item within the list
# initialize an integer named paper_to_order_total_amount at 0 which represents the entire surface area of all the present combined
# loop through the list and for each item in the list find the specific dimensions and store them in their respective integer variables
# e.g. if an item in the list is 2x3x4 then store 2 in an integer variable name length, store 3 in one called width and store 4 in one called height
# when i have all the dimensions for a given item in the list create 3 more variables named length_x_width, width_x_height, height_x_length and store the values of length*width, width*height and height*length respectively
# perform the calculation 2*length_x_width + 2*width_x_height + 2* height_x_length and store that value in a variable named surface_area
# check which of the 3 variables length_x_width, *width_x_height, height_x_length is smallest and add that value to surface area
# add the value of surface_area to paper_to_order_total_amount
# once the paper_to_order list has been looped through output the value of paper_to_order_amount
import re

paper_to_order_file = open("order_list.txt", "r")
paper_to_order = paper_to_order_file.read()
dimensions_list = paper_to_order.split("\n")

paper_to_order_total = 0

for dimensions in dimensions_list:
    length = int((re.findall("(\d+)x\d+x\d+", dimensions))[0])
    width = int((re.findall("\d+x(\d+)x\d+", dimensions))[0])
    height = int((re.findall("\d+x\d+x(\d+)", dimensions))[0])

    length_x_width = length*width
    smallest_surface_area = length_x_width

    width_x_height = width*height
    if width_x_height < smallest_surface_area:
        smallest_surface_area = width_x_height

    height_x_length = height*length
    if height_x_length < smallest_surface_area:
        smallest_surface_area = height_x_length

    surface_area = 2 * (length_x_width + width_x_height + height_x_length)

    paper_to_order_total = paper_to_order_total + surface_area + smallest_surface_area

print(paper_to_order_total)