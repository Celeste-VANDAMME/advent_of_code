# -------------------
# ADVENT OF CODE
# 2024
#
# Link:
# https://adventofcode.com/2024/day/4
# 
# Program:
#   #4-A
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
SEARCHED_WORD = "XMAS"
SEARCHED_WORD_LENGTH = len( SEARCHED_WORD )



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


# HORIZONTAL LEFT>RIGHT
def wordSearch_HLR( textInput:list ) -> int:
    
    # -- Variables
    wordCounter = int( 0 )

    
    for line in textInput:
        
        # We iterate through all the letters (except the last ones, as we will be out of range).
        for i in range( len(line) - SEARCHED_WORD_LENGTH + 1 ):
            
            if line[i:i+SEARCHED_WORD_LENGTH] == SEARCHED_WORD:
                wordCounter += 1
        
    
    # We've counted all the existing word horizontaly, from left to right.
    # We end the function here.
    
    return wordCounter
    

def lineOrderReverser( textInput:list ) -> int:
    
    # Copy that will be returned:
    textInputReversed = textInput.copy()
    
    # For each line inside the text, we reverse it!
    for lineIndex in range(len(textInput)):
        
        textInputReversed[lineIndex] = textInput[lineIndex][::-1]
    
    return textInputReversed


# VERTICAL TOP>DOWN
def wordSeach_VTD( textInput:list ) -> int:
    
    # -- Variables
    wordCounter = int( 0 )
    
    rowNB = len( textInput )
    columnNB = len( textInput[0] )    
    
    # -- Program
    
    # We will iterate through each column, from top to bottom.
    # Then, we check if the searched word is within the scanned areas.
    
    for columnIndex in range( columnNB ):
        for rowIndex in range( rowNB - SEARCHED_WORD_LENGTH + 1 ):
            
            # We create the word from each columns into a single variable
            analyzedWord = ""

            for columnLetterSearchOffset in range( SEARCHED_WORD_LENGTH ):
                analyzedWord += textInput[rowIndex + columnLetterSearchOffset][columnIndex]
            
            # Then, we can compare the selection to the searched word
            if analyzedWord == SEARCHED_WORD:
                wordCounter += 1
    
    
    # -- Final result
    return wordCounter


# VERTICAL DOWN>TOP
def wordSeach_VDT( textInput:list ) -> int:
    
    # -- Variables
    wordCounter = int( 0 )
    
    rowNB = len( textInput )
    columnNB = len( textInput[0] )    
    
    # -- Program
    
    # We will iterate through each column, from top to bottom.
    # Then, we check if the searched word is within the scanned areas.
    
    for columnIndex in range( columnNB ):
        for rowIndex in range( rowNB - 1 , SEARCHED_WORD_LENGTH - 2, -1 ):
            
            # We create the word from each columns into a single variable
            analyzedWord = ""

            for columnLetterSearchOffset in range( SEARCHED_WORD_LENGTH ):
                analyzedWord += textInput[rowIndex - columnLetterSearchOffset][columnIndex]
            
            # Then, we can compare the selection to the searched word
            if analyzedWord == SEARCHED_WORD:
                wordCounter += 1
    
    
    # -- Final result
    return wordCounter


def searchWordCounter( text:str, word:str = SEARCHED_WORD ) -> int:
    
    # -- Variables
    wordCounter = int( 0 )
    i = int(0)
    
    # -- Process
    
    # Checking if we're not out of bond for further check
    while ( i + len(word) ) <= ( len(text) ):
        
        if( text[i:i+len(word)] == word ):
            wordCounter += 1

        # Move i cursor for next iteration:
        i += 1
    
    
    # We've analyzed the text completely.
    return wordCounter


# DIAGONAL RIGHT>LEFT
def wordSeach_DRL( inputLines:list ) -> int:
    
    # -- Variables
    wordCounter = int( 0 )
    analyzedTextSequence = ""
    i = int(0)
    j = int(0)
    
    # -- Process
    
    # 1. We're going to cycle in 2 steps:
    #   a. Horizontally starting at (0,0), then going to (0,max).
    #   b. Vertically starting at (1,max), then going to (max,max) of the input
    # 
    # 2. The goal is to read the diagonal by appending the letter one after the others.
    # Then, we get the read letter sequence to a searched word detector.
    #
    # 3. We return the total of searched word detected at the end of the cycle in step 1.


    # 1. a.
    for i in range( len(inputLines[0]) ):
        
        j = 0
        analyzedTextSequence = ""
        
        # Scanning all the diagonal up to the (0, max) point:
        while i >= 0 and j < len(inputLines):
            analyzedTextSequence += inputLines[j][i]
            j += 1
            i -= 1
            
            
        # Analyzing the sequence:
        wordCounter += searchWordCounter( analyzedTextSequence )        # Right > Left
        wordCounter += searchWordCounter( analyzedTextSequence[::-1] )  # Left  > Right
       
    
    # 1. b.
    # Same process, but we analyze while going down row-wise.
    for j in range( 1, len(inputLines ) ):
        
        i = len(inputLines[0]) - 1
        analyzedTextSequence = ""
        
        while i >= 0 and j < len(inputLines):
            analyzedTextSequence += inputLines[j][i]
            j += 1
            i -= 1
        
        # Analyzing the sequence:
        wordCounter += searchWordCounter( analyzedTextSequence )        # Right > Left
        wordCounter += searchWordCounter( analyzedTextSequence[::-1] )  # Left  > Right
    
    
    # We've scanned all the diagonals once.
    return wordCounter
    

# DIAGONAL LEFT>RIGHT
def wordSeach_DLR( inputLines:list ) -> int:
    
    # -- Variables
    wordCounter = int( 0 )
    analyzedTextSequence = ""
    i = int(0)
    j = int(0)
    
    # -- Process
    
    # 1. We're going to cycle in 2 steps:
    #   a. Horizontally starting at (0,max), then going to (0,0).
    #   b. Vertically starting at (1,0), then going to (max,0) of the input
    # 
    # 2. The goal is to read the diagonal by appending the letter one after the others.
    # Then, we get the read letter sequence to a searched word detector.
    #
    # 3. We return the total of searched word detected at the end of the cycle in step 1.


    # 1. a.
    for i in range( len(inputLines[0]) - 1, -1, -1 ):
        
        j = 0
        analyzedTextSequence = ""
        
        # Scanning all the diagonal up to the (0, max) point:
        while ( j < len(inputLines) ) and ( i < len(inputLines[j] ) ):
            
            # print( "i", i, "j=",j)
            analyzedTextSequence += inputLines[j][i]
            j += 1
            i += 1
        
        
        # Analyzing the sequence:
        wordCounter += searchWordCounter( analyzedTextSequence )        # Right > Left
        wordCounter += searchWordCounter( analyzedTextSequence[::-1] )  # Left  > Right
       
    
    # 1. b.
    # Same process, but we analyze while going down row-wise.
    for j in range( 1, len(inputLines) ):
        
        i = 0
        analyzedTextSequence = ""
        
        # Scanning all the diagonal up to the (0, max) point:
        while ( j < len(inputLines) ) and ( i < len(inputLines[j] ) ):
            
            # print( "i", i, "j=",j)
            analyzedTextSequence += inputLines[j][i]
            j += 1
            i += 1

        
        # Analyzing the sequence:
        wordCounter += searchWordCounter( analyzedTextSequence )        # Right > Left
        wordCounter += searchWordCounter( analyzedTextSequence[::-1] )  # Left  > Right    
    
    
    # We've scanned all the diagonals once.
    return wordCounter



# --- C. main.py

def main():
    
    # -- 1. Input read    
    inputLines = inputReading()
    
    
    # -- 2. Counting all the searched word in the text
    totalWordDetected = int( 0 )
    
    # Horizontal search:
    totalWordDetected += wordSearch_HLR( inputLines )
    totalWordDetected += wordSearch_HLR( lineOrderReverser( inputLines ) )
    
    # Vertical search:
    totalWordDetected += wordSeach_VTD( inputLines )
    totalWordDetected += wordSeach_VDT( inputLines )
    
    # Diagonal search:
    totalWordDetected += wordSeach_DRL( inputLines )
    totalWordDetected += wordSeach_DLR( inputLines )
    
    # Result:
    print( "TOTAL DETECTED:", totalWordDetected )
    
    
    # Closing "main()"
    return



# --- D. main() execution

main()