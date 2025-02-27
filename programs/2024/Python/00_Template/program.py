# -------------------
# ADVENT OF CODE
# 2024
#
# Link:
# https://adventofcode.com/2024/day/X #TODO: replace "X" by n° of challenge
# 
# Program:
#   #<X>-<AB> # TODO: With, <X> the index of the challenge, <AB> for each solution A or B of the challenge.
# 
# Program title:
#   <TITLE> # TODO: replace the title here
#
# DEV:
#   - Celeste VANDAMME
#       GitHub: https://github.com/Celeste-VANDAMME
#       Discord: @slak3r
#
# -------------------



# --- A. GLOBAL PARAMETERS

INPUT_FILE_DIR = "programs/2024/Python/xxx/xxx.txt" # TODO: replace text directory here


# --- B. FUNCTIONS

def inputReading( ) -> list :
    """
    Reads the input from the file specified by `INPUT_FILE_DIR` and returns
    each line as an element in a list.

    Returns:
        list: A list of strings, where each string is a line from the input file.
    """
        
    rawInputLines = []
    
    with open(INPUT_FILE_DIR, "r") as input_file:
    
        for line in input_file:
            rawInputLines.append( line )
    
    
    # Let's remove the "\n" out of the file
    for i in range( len(rawInputLines) ):
        rawInputLines[i] = rawInputLines[i].replace( "\n", "" )
    
    
    # The lines have properly been read
    return rawInputLines


# --- C. main.py

def main():
    
    # -- 1. Input read    
    inputLines = inputReading()
    
    
    # -- 2. (...)
    
    
    # Closing "main()"
    return


# --- D. main() execution

main()