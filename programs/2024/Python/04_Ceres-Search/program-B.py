# -------------------
# ADVENT OF CODE
# 2024
#
# Link:
# https://adventofcode.com/2024/day/4
# 
# Program:
#   #4-B
# 
# Program title:
#   Ceres Search
#
# DEV:
#   - Celeste VANDAMME
#       GitHub: https://github.com/Celeste-VANDAMME
#       Discord: @slak3r
#
# -------------------



# --- A. GLOBAL PARAMETERS

INPUT_FILE_DIR = "programs/2024/Python/04_Ceres-Search/input.txt"



# --- B. FUNCTIONS

def inputReading( ) -> list:
        
    rawInputLines = []
    
    with open(INPUT_FILE_DIR, "r") as input_file:
    
        for line in input_file:
            rawInputLines.append( line )
    
    
    # Let's remove the "\n" out of the file
    for i in range( len(rawInputLines) ):
        rawInputLines[i] = rawInputLines[i].replace( "\n", "" )
    
    
    # The lines have properly been read
    return rawInputLines


def isAreaXMAS(text:list, i:int, j:int) -> bool:
    
    # -- Variables:
    textDiagonal_LR             = str("")
    textDiagonal_LR_reverse     = str("")
    
    textDiagonal_RL             = str("")
    textDiagonal_RL_reverse     = str("")
    
    # -- Process:
    
    # 1. Scanning the area of the (i,j) location:
    
    # a. Diagonal Left Right:
    for scanLength in range( -1, 2, 1 ):
        textDiagonal_LR += text[i+scanLength][j+scanLength]
    
    textDiagonal_LR_reverse = textDiagonal_LR[::-1]
    
    
    # b. Diagonal Right Left:
    for scanLength in range( -1, 2, 1 ):
        textDiagonal_RL += text[i+scanLength][j-scanLength]
    
    textDiagonal_RL_reverse = textDiagonal_RL[::-1]

    
    # 2. Now checking if the x-mas condition is ok:
    if (textDiagonal_LR == "MAS" or textDiagonal_LR_reverse == "MAS") and (textDiagonal_RL == "MAS" or textDiagonal_RL_reverse == "MAS"):
        return True
    
    else:
        return False


def xmasDetection_B( text:list ) -> int:
    
    # -- Variables:
    xmasCounter = int(0)
    letter = str("")
    
    i = int(0)
    j = int(0)
        
    # -- Process:
    
    # We scan the text to find all the "A".
    # "A" is an interesting letter, as it's the center of each "X-MAS".
    #
    # Note that we cycle through the text, except on its border (1,0) TO (1, (len-1)).
    
    for i in range(1, len(text) - 1):
        for j in range(1, len(text[i]) - 1):
            
            if text[i][j] == "A":
                if isAreaXMAS( text, i, j):
                    
                    # If we found a valid x-mas area, we count it!
                    xmasCounter += 1
    
    # We've checked for the whole text.
    # Thus, all the possible x-mas were found!
    
    return xmasCounter




# --- C. main.py

def main():
    
    # -- 1. Input read    
    inputLines = inputReading()
    
    
    # -- 2. Counting all the searched word in the text
    totalWordDetected = int( 0 )
    
    # -- 3. X-MAS detection
    totalWordDetected = xmasDetection_B( inputLines )
    
    # Result:
    print( "TOTAL DETECTED:", totalWordDetected )
    
    
    # Closing "main()"
    return



# --- D. main() execution

main()