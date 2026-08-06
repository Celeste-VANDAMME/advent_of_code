# [>] LIBRARIES
# ---------------------
from pathlib import Path
from dataclasses import dataclass


# [>] DATA CLASS
# ---------------------
@dataclass
class LineInfo:
    string_code_len: int
    memory_value_len: int


# [>] GLOBAL VARIABLES
# ---------------------
input_path = Path("programs/2015/Python/08/input.txt")


# [>] FUNCTIONS
# ---------------------
def file_reading() -> list[str]:

    data = input_path.read_text(encoding="utf-8").splitlines()
    return data


def memory_length( line:str ) -> int:

    # Starting from the usual length, and removing the "" characters already!
    clear_line = line[1:-1]
    line_memory_length = len(clear_line)
    

    # Now we check for each potential escape characters

    index_esc_char = 0
    index_start_lookup = 0

    while index_esc_char != -1:
        index_esc_char = line.find( "\\", index_start_lookup)

        # If we find the esc. character, then let's remove it from the char. count
        if index_esc_char != -1 :

            next_char = line[index_esc_char+1]

            if next_char in ("\\", '"') :
                line_memory_length -= 1 # from "\\" to "\" (2 to 1)

                # Also, we will keep looking for what's after the found: "\(...)" for the next loop
                index_start_lookup = index_esc_char + 2


            # HEXA esc., format: \x65 >> 
            elif next_char == "x":
                line_memory_length -= 3 # "\x23" > "f" (from 4 to 1)
                
                # Also, we will keep looking for what's after the found: "\(...)" for the next loop
                index_start_lookup = index_esc_char + 4

            else:
                raise ValueError( "An unknown value was found after \\, line:", line )


    return line_memory_length


# [>] MAIN() FUNCTION
# ---------------------
def main() -> int:

    data = file_reading()

    line_info : list[LineInfo] = []

    for line in data:

        string_code_length = len( line )
        memory_value_length = memory_length( line )

        line_info.append( LineInfo( string_code_length, memory_value_length) )

    # Let's get the total out of all the input!
    delta_sum = sum( 
        line.string_code_len - line.memory_value_len 
        for line in line_info )

    print( delta_sum )

    return 0


# [>] main() launcher
# ---------------------
if __name__ == "__main__":
    main()








