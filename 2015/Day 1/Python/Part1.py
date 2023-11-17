# ( means santa should go up one floor
# ) means santa should go down one floor
# Santa starts at floor 0, the building is very tall and very deep

# Start an integer at 0, read the file and store the contents into its own variable called floor_number, break that variable down character by character
# If the character is a ( then add one to floor_number, if the character is ) then take 1 from floor_number

instructions_file = open("../instructions.txt", "r")
instructions = (instructions_file.read())

floor_number = 0

for instruction in instructions:
    if instruction == "(":
        floor_number = floor_number + 1
    elif instruction == ")":
        floor_number = floor_number - 1

print(floor_number)