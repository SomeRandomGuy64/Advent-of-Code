# Santa starts at a house and delivers a present to it
# he has a set of instructions detailing which direction to go, ^ for north, > east, v south, < west
# after every instruction he delivers the present to the house he is at, regardless of if they already have a present
# how many houses receive at least one present?

# use a coordinate system as well as a set
# for the current location store the current location in the tuple
# find the length of the map

instructions_file = open("instructions.txt", "r")
instructions = instructions_file.read()

coordinates = set()

x_coordinate = 0
y_coordinate = 0

coordinates.add((x_coordinate, y_coordinate))

for instruction in instructions:

    if instruction == "^":
        y_coordinate += 1
    if instruction == "v":
        y_coordinate -= 1
    if instruction == ">":
        x_coordinate += 1
    if instruction == "<":
        x_coordinate -= 1

    coordinates.add((x_coordinate, y_coordinate))

print(len(coordinates))