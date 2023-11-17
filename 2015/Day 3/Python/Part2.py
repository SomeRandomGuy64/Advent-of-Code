# Santa starts at a house and delivers a present to it, so does Robo-Santa
# he has a set of instructions detailing which direction to go, ^ for north, > east, v south, < west
# after every instruction he delivers the present to the house he is at, regardless of if they already have a present
# however this time santa only follow every other instruction, robo santa then follows the instructions santa hasn't
#e.g. ^><v  they both start at the same house, sant goes ^ then robo-santa goes >, santa goes < then robo santa goes v
# how many houses receive at least one present?

# use a coordinate system as well as a set
# for the current location store the current location in the tuple
# find the length of the map

instructions_file = open("../instructions.txt", "r")
instructions = instructions_file.read()

coordinates = set()

santa_x_coordinate = 0
santa_y_coordinate = 0

robo_santa_x_coordinate = 0
robo_santa_y_coordinate = 0

coordinates.add((0, 0))

def traverse_insturctions(x_coordinate, y_coordinate, instruction):
    if instruction == "^":
        y_coordinate += 1
    if instruction == "v":
        y_coordinate -= 1
    if instruction == ">":
        x_coordinate += 1
    if instruction == "<":
        x_coordinate -= 1

    coordinates.add((x_coordinate, y_coordinate))

    return x_coordinate, y_coordinate

turn = 1

for instruction in instructions:
    if turn % 2 == 1:
        santa_x_coordinate, santa_y_coordinate = traverse_insturctions(santa_x_coordinate, santa_y_coordinate, instruction)
    else:
        robo_santa_x_coordinate, robo_santa_y_coordinate = traverse_insturctions(robo_santa_x_coordinate, robo_santa_y_coordinate, instruction)

    turn += 1

print(len(coordinates))