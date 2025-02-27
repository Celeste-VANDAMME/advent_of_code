# -------------------
# ADVENT OF CODE
# 2024
#
# Link:
# https://adventofcode.com/2024/day/5
# 
# Program:
#   #05-AB
# 
# Program title:
#   "Print Queue"
#
# DEV:
#   - Celeste VANDAMME
#       GitHub: https://github.com/Celeste-VANDAMME
#       Discord: @slak3r
#
# -------------------



# --- A. DEPENDANCIES

from math import ceil
from itertools import permutations


# --- B. GLOBAL PARAMETERS

INPUT_FILE_DIR = "programs/2024/Python/05_Print_Queue/sample.txt"



# --- C. FUNCTIONS

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


def inputSeparator( input:list ) -> tuple[list,list]:
    
    i = int(0)
    isEmptyLineFound = False
    
    # We cycle through the whole input until we find the empty line between ordering rules & updates.
    for i in range(len( input )):
        
        if( input[i] == "" ):
            isEmptyLineFound = True
            break
    
    
    # Once found, we return the two lists here:
    if isEmptyLineFound:
        return input[0:i], input[i+1:]
    
    # If nothing has been found, cast an error and stop the program:
    else:
        raise Exception( "Couldn't find the empty line separator in data. Please make sure you're using the right 'input.txt' file, provided by Advent of Code." )


def orderingRuleCompiler( input:list ) -> dict:
    """
    Compiles ordering rules from input.
    
    Format:
    {
        pageNumber: [updatePossible (list)]
    }
    
    Example:
    {
        17: [1, 3, 93, 95],
        29: [2, 39],
        ...
    }
    """
    
    # VARIABLES:
    
    # Using a DICTIONARY to hold the rules will greatly improve performance over a list.
    orderingRules = {}
    
    
    # PROGRAM:
    
    for orderLine in input:
        
        # 1/ Parse the line into integers:
        pageNumber, updatePageNumberAllowed = map(int, orderLine.split("|"))
        
        # 2.a/ Update the rule (if already existing):
        if pageNumber in orderingRules:
            orderingRules[pageNumber].append(updatePageNumberAllowed)
            orderingRules[pageNumber].sort()
            
        # 2.b/ Add the rule:
        else:
            orderingRules[pageNumber] = [updatePageNumberAllowed]

    
    return orderingRules
    
    
    # ARCHIVE:
    
    # "LIST" version of the program (instead of dictionary):
    """
    for orderLine in input:
        
        # Get the 1st and 2nd element splitted:
        pageNumber, updatePageNumberAllowed = map( int, orderLine.split( "|" ) )
        
        
        # Then, we cycle through the ordering rule list to find if the "pageNumber" already exists.
        # Otherwise, we will have to create the input first.
        
        # 1/ Variables
        isPageNumberExistingInRules = False
        
        # 2/ Cycling through the orderingRules matrice
        #    to perhaps find if we already created rules for the looked pageNumber value.
        for i in range(len(orderingRules)):
            
            # 3.a/ If the number already have rules, then we only append the value to it.
            if orderingRules[i][0] == pageNumber:
                
                orderingRules[i][1].append( updatePageNumberAllowed )
                isPageNumberExistingInRules = True
                
                break
        
        
        # 3.b/ Create the index for the unfound pageNumber value
        if not(isPageNumberExistingInRules):
            orderingRules.append( [pageNumber, [updatePageNumberAllowed]] )
    """


def sequenceChecker( checkedSequence:list, referenceSequence:list ) -> bool:
    
    # VARIABLES:
    isCheckedSequenceInReference = True
    isValueInReference = False
    
    # PROGRAM:
    
    """
    We iterate through all the values in the checked sequence.
    The goal is to check if all the values are included in the reference (A-1).
    
    If they're, then the boolean "isCheckedSequenceInReference" keeps its "True" value 
    up until the end (A-2)! Otherwise it will get flipped to "False" and the loop stops.
    """
    
    for checkSequenceValue in checkedSequence:
        
        # Reset for each loop:
        isValueInReference = False
        
        for referenceValue in referenceSequence: # (A-1)
            
            if checkSequenceValue == referenceValue: # (A-1)
                isValueInReference = True
                break
    
        if not(isValueInReference): # (A-2)
            isCheckedSequenceInReference = False
            break
    
    
    # We've checked everything:
    return isCheckedSequenceInReference


def updateAnalyzer( input:list, orderingRules:dict ) -> list:
    
    # VARIABLES:
    validUpdate = [] # Returned list containing the OK updates
    isUpdateLineValid = True
    
    # PROGRAM:
    
    for updateLine in input:
        
        # Starting with the assumption that the line is OK,
        # Then, it might get unvalidated after analyzing it.
        isUpdateLineValid = True
        
        
        # Cleaning the line for proper values:
        rowNumbers = updateLine.split(",")
        
        # We cycle through all the numbers up to the second to last
        # to check if the update is allowed in the orderingRules dict.
        for numberIndex in range(len(rowNumbers) - 1):
            
            checkedPageNumber   = int( rowNumbers[numberIndex] )
            nextPageNumbers     = list( map( int, rowNumbers[numberIndex+1:] ) )

            try:
                if not( sequenceChecker(nextPageNumbers, orderingRules[checkedPageNumber]) ):
                    isUpdateLineValid = False
                    break
            
            # IF: we checked a value not existing in orderingRules, then we reject the line
            except KeyError:
                isUpdateLineValid = False
                break
        
        
        # All components of the line has been fully analyzed.
        if isUpdateLineValid:
            validUpdate.append( updateLine )
    
    
    # The entire input has been checked.
    return validUpdate


def medianValueCalculator_A( input:list ) -> int:
    
    # VARIABLES
    medianSum = int(0)
    
    
    # PROGRAM
    
    for line in input:
        
        # 1. Converting STR input to distinct INT:
        lineValues = list(map( int, line.split( "," ) ))
        
        # 2. Finding the median:
        medianIndex = ceil( len(lineValues) / 2 ) - 1
        
        # 3. Sum it:
        medianSum += lineValues[medianIndex]
    
    
    # All the lines have been processed
    return medianSum


def resultPrinting_A( medianSum:int ) -> None:
    
    print()
    print( " >> RESULT <<")
    print( "The median sum value is:", medianSum )
    print()

    return None


def deniedUpdateSorter( updateInput:list, validUpdate:list ) -> list:
    
    
    invalidUpdate = list( set(updateInput) ^ set(validUpdate) )
    
    
    return invalidUpdate
    

def invalidUpdateFix( invalidUpdates:list, orderingRules:dict ) -> list:
    
    # VARIABLES:
    fixedUpdates = []
    
    
    # PROGRAM:
    
    for invalidUpdate in invalidUpdates:
        
        print( "Invalid update:", invalidUpdate )


# --- D. main.py

def main():
    
    # -- 1. Input read    
    inputLines = inputReading()
    
    # -- 2. Separating the input data into "ordering rules" and "update" properly 
    orderingRulesInput, updateInput = inputSeparator( inputLines )
    
    # -- 3. Creating an ordering rules dictionary, for all allowed update pages
    orderingRules = orderingRuleCompiler( orderingRulesInput )
    
    # -- 4. Analyze the update input for valid lines
    validUpdate = updateAnalyzer( updateInput, orderingRules )
    
    # -- 5. Adding the median value for each valid update
    middleValueSum_A = medianValueCalculator_A( validUpdate )
    
    # -- 6. Display the result!
    resultPrinting_A( middleValueSum_A )
    
    # -- 7. Getting the invalid updates that got rejected
    invalidUpdates = deniedUpdateSorter( updateInput, validUpdate )
    invalidUpdates_int = [ list(map(int, line.split(",")) ) for line in invalidUpdates ]
    
    # -- 8. Applying a fix for each invalid update
    fixedUpdates_B = invalidUpdateFix( invalidUpdates_int, orderingRules )
    
    
    
    # Closing "main()"
    return None


# --- E. main() execution

main()