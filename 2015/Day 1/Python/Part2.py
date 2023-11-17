# Find the position of the first character that causes Santa to enter the basement
# The first character is position 1, second is position 2 and so on

# Read the file and store the contents in a variable named instructions
# initialize an integer variable called floor_number that represents the current floor santa is one
# initialize an integer variable call instruction_position which represents the position of the current instruction 
# loop through the instructions, every time the character is ( add one to floor_number, every time the character is ) take one to floor_number
# one the floor_number reaches -1 break out of the loop and output instruction_position

instructions_file = open("../instructions.txt", "r")
instructions = instructions_file.read()

floor_number = 0
instruction_position = 0

for instruction in instructions:
    if floor_number == -1:
        break

    if instruction == "(":
        floor_number += 1
    elif instruction == ")":
        floor_number -= 1
    
    instruction_position += 1

print(instruction_position)
