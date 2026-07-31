# - Libraries
# ---------------------
from dataclasses import dataclass


# - Data class (it's like structures in C)
# ---------------------
@dataclass
class LineInstruction:
    start: tuple[int, int]
    end: tuple[int, int]
    action: str


# - File reading
# ---------------------
data_directory = "programs/2015/Python/06/input.txt"

with open(data_directory, "r") as data_file:
    input_data = data_file.read()


# Print the result:
# print( input_data )


# - File into data
# ---------------------

# I'm aiming for a 2D into 2D list
# This type:
# array = [
# [ (10, 20), (15, 30), "on"],
# [ (20, 50), (35, 60), "toggle"],
# ...
# ]

instruction_array: list[LineInstruction] = []


for line in input_data.splitlines():

    line_parts = line.split()

    # [>] Action
    if line_parts[0] == "toggle":
        action = "toggle"
        x1, y1 = map(int, line_parts[1].split(","))
        x2, y2 = map(int, line_parts[3].split(",")) 

    else:
        if line_parts[1] == "off":
            action = "off"

        elif line_parts[1] == "on":
            action = "on"

        else:
            raise ValueError( "Invalid instruction: ", line )

        # [>] Coordinate
        x1, y1 = map(int, line_parts[2].split(","))
        x2, y2 = map(int, line_parts[4].split(","))


    # [>] Saving the line in the instruction array
    instruction = LineInstruction( (x1, y1), (x2, y2), action)
    instruction_array.append( instruction )

    #C-Programming way (char by char)
    """
    # >> Action: turn on/off or toggle
    if( line[0:8] == "turn off" ):
        buffer_action = "Turn off"
        buffer_action_ID = -1

        line_reading_position = 9

    elif( line[0:7] == "turn on" ):
        buffer_action = "Turn on"
        buffer_action_ID = 1

        line_reading_position = 8

    elif( line[0:6] == "toggle" ):
        buffer_action = "Toggle"
        buffer_action_ID = 0

        line_reading_position = 7
        

    else:
         print("ERROR WITH AN INPUT LINE:", line)
         exit()

    """


# [>] Light grid (1000x1000)
# This grid contains binary values: either the light is turned on (1) or off (0).

grid = [ [0 for _ in range(1000)] for _ in range(1000) ]

for instruction in instruction_array:

    x_init = instruction.start[0]
    y_init = instruction.start[1]

    if instruction.action == "on":

        for row_range in range( instruction.end[1] - instruction.start[1] + 1 ):
            for column_range in range( instruction.end[0] - instruction.start[0] + 1 ):

                grid[y_init + row_range][x_init + column_range] = 1

                # Debug:
                #print(f"Value changed: array[{x_trigger}][{y_trigger}]")


    elif instruction.action == "off":

        for row_range in range( instruction.end[1] - instruction.start[1] + 1 ):
            for column_range in range( instruction.end[0] - instruction.start[0] + 1 ):

                grid[y_init + row_range][x_init + column_range] = 0


    elif instruction.action == "toggle":

        for row_range in range( instruction.end[1] - instruction.start[1] + 1 ):
            for column_range in range( instruction.end[0] - instruction.start[0] + 1 ):

                if grid[y_init + row_range][x_init + column_range] == 0:
                    grid[y_init + row_range][x_init + column_range] = 1

                else:
                    grid[y_init + row_range][x_init + column_range] = 0


# [>] Now summing all the lights ON (= 1)
light_on_count = sum( row.count(1) for row in grid )

print( "Amount of light on at the end of instructions:", light_on_count )

    
    



    








