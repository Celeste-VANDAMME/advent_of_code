# -------------------
# ADVENT OF CODE
# 2024
#
# Link:
# https://adventofcode.com/2024/day/2
# 
# Program:
#   #1-B
# 
# Program title:
#   Red-Nosed Reports
#
# DEV:
#   - Celeste VANDAMME
#       GitHub: https://github.com/Celeste-VANDAMME
#       Discord: @slak3r
#
# -------------------


# --- A. GLOBAL PARAMETERS

# Error dampener
isErrorDampenerActive = True

# Difference range for each level
lower_delta_range = int( 1 )
upper_delta_range = int( 3 )


# --- B. FUNCTIONS

def isReportSafe( input_report ):
    
    # Copying the input list for further manipulation
    report = input_report.copy()
    
    shouldReportIncrease = None         # BOOLEAN: state if the report should have increasing/decreasing values!
    hasErrorDampenerBeenUsed = False    # BOOLEAN: have we removed one level of the report yet?
    i_offsetActivated = False           # BOOLEAN: if an error has been detected, "i" in the main loop have to be offset by -1 !
    
    # -- 1. Checking the trend (increasing/decreasing).
    # We have to cycle through the 3 first elements of the list in case we have identical values (e.g.: [4 4 6 5 12] (line 59) )...
    # Because we can now get ride of a level if the problem dampener is active!
    
    for i in range( 2 ) :
        
        # If there've been an issue with the previous loop, we move the i backward by one cell.
        if( i_offsetActivated ):
             i -= 1
        
        value_1 = report[i]
        value_2 = report[i+1]
        
        if  ( value_1 < value_2 ):
            shouldReportIncrease = True
            break
        
        elif( value_1 > value_2 ):
            shouldReportIncrease = False
            break
        
        else: # the elements are equal!
            
            if  ( not(hasErrorDampenerBeenUsed) ):
                # We choose to get ride of the 2nd element that is equal
                # (It doesn't really matter, as we get ride of the very same element!)
                report.pop(i+1)
                i_offsetActivated = True # As we've removed one element of the list, we decrease the array cursor one way backward too.
                hasErrorDampenerBeenUsed = True
                
            # If we already have pop a level out of the report, then the report is unsafe anyway    
            elif( hasErrorDampenerBeenUsed ):
                print( "1. IN FUNCTION =", report )
                return False
                
                        

    # Even though it is not really useful, we reset the i_offset here:
    i_offsetActivated = False
    
    # This isn't used at all, because now the parameter "hasErrorDampenerBeenUsed" is True.
    # So, it's primarily just to not activate the same backward phenomenom for the next loop.


    # We cycle through all the elements of the report except the last one:
    for i in range( len( report[:-1] ) ) :
        
        # If the previous cycle had an error detected...
        # Meaning, an element pop'ed out of the report.
        
        # We have to offset the i by 1 every cycle from now on!
        if( i_offsetActivated ):
             i -= 1
        
        value_1 = report[i]
        value_2 = report[i+1]    
        
        hasCycleAnError = False
        
        # -- 1. Checking the trend (increasing/decreasing).
        if  ( value_2 - value_1 > 0 and shouldReportIncrease == False ):
            hasCycleAnError = True
        
        elif( value_2 - value_1 < 0 and shouldReportIncrease == True ):
            hasCycleAnError = True
        
        # -- 2. Check if the difference between each element is included in the range: [1;3].     
        # We check here if the difference is beyond the range:
        if( 
           abs( value_2 - value_1 ) < lower_delta_range 
           or abs( value_2 - value_1 ) > upper_delta_range ):
            
            # If that is true once, then the report is unsafe. :(
                hasCycleAnError = True
        
        # Let's see if the cycle contained an error in the process:
        if( hasCycleAnError ):
            if  ( not(hasErrorDampenerBeenUsed) ):
                report.pop(i+1)             # We get ride of the 2nd element
                
                hasErrorDampenerBeenUsed = True
                i_offsetActivated = True    # As we've removed one element of the list, we decrease the array cursor one way backward too.
            
            # If we already have pop a level out of the report, then the report is unsafe anyway    
            elif( hasErrorDampenerBeenUsed ):
                print( "1. IN FUNCTION =", report )
                return False
                
        
    # Now that we've done all the tests on the report
    # We know that it's safe!
    # print( "1. IN FUNCTION =", report )
    return True        


# --- C. Input reading

reports         = [] # This will hold all the reports, line by line
report_buffer   = [] # This will be only used to construct the "reports" array

with open("programs/2024/Python/02_Red-Nosed-Reports/input.txt", "r") as input_file:
    
    for line in input_file:
        
        # Getting from "7 6 4 2 1\n" to "[7, 6, 4, 2, 1]":
        report_buffer = [int(value) for value in line.strip("\n").split(" ")]
        
        # Then saving the data in the global
        reports.append( report_buffer )
        
# Display result:
# print( reports )      # All the array
# print( reports[0] )   # Only the first line


# --- D. Report Safety Check (RSC)

# Let's now check if each report is safe, and keep count of each.
safe_reports_counter = int( 0 )

for report in reports:
    
    # Using the dedicated function to check
    if( isReportSafe( report ) ):
        safe_reports_counter += 1
        # print( "2. BACKUP =", report )

    
# We found the total amount of safe reports!
print( "Number of safe reports in the input:", safe_reports_counter )



