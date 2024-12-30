# -------------------
# ADVENT OF CODE
# 2024
#
# Link:
# https://adventofcode.com/2024/day/2
# 
# Program:
#   #2-A
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

# --- A. FUNCTIONS

def isReportSafe( report ):
    
    shouldReportIncrease = None     # BOOLEAN: state if the report should have increasing/decreasing values!
    
    # -- 1. Checking the trend (increasing/decreasing).
    # We don't have to cycle through all the list in case we have identical values (e.g.: [4 4 6 5 12] (line 59) )...
    # Because the condition #2 of having a difference included in the [1;3] range will be invalidated!
    # Thus, the report will be considered unsafe.
    
    if  ( report[0] < report[1] ):
        shouldReportIncrease = True
    
    elif( report[0] > report[1] ):
        shouldReportIncrease = False
    
    else: # the elements are equal!
        return False
        
    
    # We cycle through all the elements of the report except the last one:
    for i in range( len( report[:-1] ) ) :
        
        value_1 = report[i]
        value_2 = report[i+1]
        
        # -- 1. Checking the trend (increasing/decreasing).
        if  ( value_2 - value_1 > 0 and shouldReportIncrease == False ):
            return False
        
        elif( value_2 - value_1 < 0 and shouldReportIncrease == True ):
            return False
        
        # -- 2. Check if the difference between each element is included in the range: [1;3].
        # Parameters:
        lower_delta_range = int( 1 )
        upper_delta_range = int( 3 )
        
        # We check here if the difference is beyond the range:
        if( 
           abs( value_2 - value_1 ) < lower_delta_range 
           or abs( value_2 - value_1 ) > upper_delta_range ):
            
            # If that is true once, then the report is unsafe. :(
                return False
        
    # Now that we've done all the tests on the report
    # We know that it's safe!
    return True        


# --- B. Input reading

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


# --- C. Report Safety Check (RSC)

# Let's now check if each report is safe, and keep count of each.
safe_reports_counter = int( 0 )

for report in reports:
    
    # Using the dedicated function to check
    if( isReportSafe( report ) ):
        safe_reports_counter += 1

    # DEBUG displays:
    print( report )
    print( isReportSafe( report ) )
    
# We found the total amount of safe reports!
print( "Number of safe reports in the input:", safe_reports_counter )



