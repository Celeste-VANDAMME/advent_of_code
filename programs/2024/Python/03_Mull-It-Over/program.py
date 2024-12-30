# -------------------
# ADVENT OF CODE
# 2024
#
# Link:
# https://adventofcode.com/2024/day/3
# 
# Program:
#   #3-A-B
# 
# Program title:
#   Mull It Over
#
# DEV:
#   - Celeste VANDAMME
#       GitHub: https://github.com/Celeste-VANDAMME
#       Discord: @slak3r
#
# -------------------


# --- A. GLOBAL PARAMETERS

INPUT_FILE_DIR = "programs/2024/Python/03_Mull-It-Over/input.txt"
IS_PROGRAM_LOOKING_FOR_DO_DONT = True # Set to "True" to activate the challenge B

MUL_CALL = "mul("
DO_CALL = "do()"
DONT_CALL = "don't()"

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
        
    return rawInputLines


def findParameterLength( line:list, i:int) -> tuple[int,bool]:
    """
    Scans the provided line for the length of the parameters inside the `mul()` call
    starting at position `i`. It stops when the closing parenthesis `)` is found.

    Args:
        line (list): The line being scanned, which contains the `mul()` call.
        i (int): The starting index of the `mul(` call in the line.

    Returns:
        tuple[int, bool]: A tuple where the first element is the length of the parameters
        inside `mul()`, and the second element is a boolean indicating if a closing
        parenthesis `)` was found.
    """
        
    # We can have a maximum of 8 letters folllowing...
    # As, we're here: 
    # "mul(" 
    # 
    # And the remaining letters should be:
    # "XXX,YYY)"
    
    # We find the length of the inside of the mul call:
    mulCallParameterLength = int(1)
    isClosingParenthesisFound = False
    
    for j in range( 8 ):
                        
        if line[ (i+4) + j] == ")":
            isClosingParenthesisFound = True    # An end of the call is properly found
            break                               # We stop the loop and will use the found length

        else:
            mulCallParameterLength += 1         # If we haven't found the end, we keep adding to the length counter

    # Once we've scanned the whole +8 text after the "mul(" call, we return the length found
    return mulCallParameterLength, isClosingParenthesisFound


def argumentsIntCheck( argumentsInput:list ) -> bool:
    """
    Checks if all elements in the provided list are numeric strings (digits only).

    Args:
        argumentsInput (list): A list of strings to check.

    Returns:
        bool: True if all elements in the list are numeric strings, False otherwise.
    """
        
    # We start with the assumption of the input being proper int
    areArgumentsInt = True
    
    # Then, we check if both of the arguments are truly digits...
    for argument in argumentsInput:
        
        if not argument.isdigit():
            areArgumentsInt = False
            break
    
    # Once we're done here, we know if all the arguments are int or not!
    return areArgumentsInt


def doDontCheck( inputText:str ) -> bool:
    """
    Checks if the given text matches the `do()` or `don't()` instructions.

    Args:
        inputText (str): The string to check.

    Returns:
        bool: True if the string is "do()", False if it is "don't()", and None if neither.
    """
    
    # -- Condition checks
    if inputText[:-3] == DO_CALL:
        return True
    
    elif inputText == DONT_CALL:
        return False
    
    else:
        return None


def mulDetector( inputLines:list ) -> list:
    """
    Scans a list of lines for valid `mul()` calls, collecting their arguments
    into a list of tuples. If the program is in a "don't" state, the function
    skips the `mul()` calls.

    Args:
        rawLines (list): A list of strings to scan for `mul()` calls.

    Returns:
        list: A list of tuples, where each tuple contains the two integer arguments
        from a valid `mul()` call.
    """
        
    # Tried with a txt.split( "mul(" ) method on the whole text, but didn't go well.
    # I'll do it the slow way by scanning all the text. ;)
    
    isDoActive = True # We start with the do() effect active to begin with
    
    mulValidCalls = []
    
    for line in inputLines:
        for i in range(len(line)):
            
            doDontSegmentAnalyzed = line[i:i+7]     # we check for "do()" or "don't()" 
            mulCallSegmentAnalyzed = line[i:i+4]    # we check for "mul("
            
            # ADDITIONAL "B" part of the program
            # ---
            if IS_PROGRAM_LOOKING_FOR_DO_DONT:
                
                # Let's check if the scanned segment contains do()/dont()
                doStatusInAnalyzedSegment = doDontCheck( doDontSegmentAnalyzed )
                
                # doStatusInAnalyzedSegment has 3 states:
                # 1. TRUE:  a "do()" is detected
                # 2. FALSE: a "don't()" is detected
                # 3. None:  Nothing has been detected
                
                # If the previous check detected something new...
                if doStatusInAnalyzedSegment is not None:
                    isDoActive = doStatusInAnalyzedSegment # we apply it to the global do/don't status
                
                
                # After having checked for the "Do()"/"Don't()" condition...
                if not isDoActive:
                    continue # We skip the current loop
                
                # Otherwise, we will do the usual mulCall check... (following the next lines ;) )
                
                            
            # ---
            if mulCallSegmentAnalyzed == MUL_CALL:
                
                # Then, we keep analyzing it for the upcoming max 8 letters!
                mulCallParameterLength, isClosingParenthesisFound = findParameterLength(line, i)

                # ---
                if isClosingParenthesisFound:
                    
                    # Let's get proper indication for "XXX,YYY" string location
                    argumentStart = i+4
                    argumentEnd = i+4+mulCallParameterLength-1
                    
                    argumentString = line[argumentStart:argumentEnd]
                    
                    # ---
                    # We have to check for integrity, in case we found a ")" but with text/space inside...
                    areArgumentsIntOnly = argumentsIntCheck( argumentString.split(",") )
                    
                    if areArgumentsIntOnly:
                    
                        # Time to convert arguments to integers
                        mulArguments = [int(arg) for arg in argumentString.split(",")]

                        
                        # The line is valid, and we found the the two arguments we will have to multiply!
                        # For now, let's keep them in a list for further processings.
                        mulValidCalls.append( mulArguments )
        
    # Now that we've scanned the whole lines for valid mul(...) calls,
    # We can now process the data ;)
    
    # Let's return the found valid calls:
    return mulValidCalls


def mulCalculation( mulCalls:list ) -> int:
    """
    Multiplies each pair of integers in the provided list and returns the sum
    of all the multiplication results.

    Args:
        mulCalls (list): A list of tuples, where each tuple contains two integers
        to multiply.

    Returns:
        int: The total sum of the multiplication results.
    """
    
    # We set a counter for all the calls:
    totalSum = int(0)
    
    # We will calculate each elements in the list!
    for x,y in mulCalls:
        totalSum += x*y
    
    # Then, once the entire calls have been added up together...
    return totalSum
    

# --- C. main.py

def main():
    
    # -- 1. Input read    
    inputLines = inputReading()
    
    # -- 2. Scanning the input for valid "mul(...)" calls:
    mulTotalCalls = mulDetector( inputLines )
    
    # -- 3. Sum all the valid call results
    totalSum = mulCalculation( mulTotalCalls )

    # -- 4. Display the result. ;)
    print( "<*> RESULT")
    print( 'Result of the "mul()" calls:',  totalSum)
    print( "" )
    print( "<*> ADDITIONNAL STATS:")
    print( 'NB of "mul()" calls:',          len(mulTotalCalls) )
    print( "AVG result of the calls:",      round( totalSum/len(mulTotalCalls), 1) )
    
    # Closing "main()"
    return


# --- D. main() execution

main()