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


# --- B. FUNCTIONS

def inputReading( ) -> list :
    
    rawInputLines = []
    
    with open(INPUT_FILE_DIR, "r") as input_file:
    
        for line in input_file:
            rawInputLines.append( line )
        
    return rawInputLines


def findParameterLength( line:list, i:int) -> tuple[int,bool]:
    
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
    
    # -- Variables for further check
    doStringCheck   = "do()"
    dontStringCheck = "don't()"
    
    # -- Condition checks
    if inputText[:-3] == doStringCheck:
        return True
    
    elif inputText == dontStringCheck:
        return False
    
    else:
        return None


def mul_detector( rawLines:list ) -> list:
    
    # Tried with a txt.split( "mul(" ) method on the whole text, but didn't go well.
    # I'll do it the slow way by scanning all the text. ;)
    
    isDoActive = True # We start with the do() effect active to begin with
    
    mulValidCalls = []
    validMulCallText = "mul("
    
    for line in rawLines:
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
            if mulCallSegmentAnalyzed == validMulCallText:
                
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
    rawLines = inputReading()
    
    # -- 2. Scanning the input for valid "mul(...)" calls:
    mulTotalCalls = mul_detector( rawLines )
    
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