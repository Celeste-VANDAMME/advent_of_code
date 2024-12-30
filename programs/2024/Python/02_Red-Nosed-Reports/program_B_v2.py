# -------------------
# ADVENT OF CODE
# 2024
#
# Link:
# https://adventofcode.com/2024/day/2
# 
# Program:
#   #2-B (v. 2)
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

isDampenerActive = True



# --- B. FUNCTIONS

def reportTrend( report:list ) -> bool :
    
    trendMeter = int( 0 )
    
    # - a. Checking the whole list to get the trend
    for i in range( len(report[:-1]) ):
        
        if( report[i] < report[i+1] ):
            trendMeter += 1
            
        if( report[i] > report[i+1] ):
            trendMeter -= 1
        
    # Now that we've been through the whole list, we have the trend
    isIncreasing = (trendMeter > 0)
        
    if trendMeter == 0:
        return None
        # raise ValueError("Trend=0, report=", report )
    
    return isIncreasing    
    

def safetyCheckRule_1( report:list ) -> bool:
    
    isIncreasing = None # BOOLEAN: Is the report increasing/decreasing?
    isRuleChecked = True # BOOLEAN: is the whole rule checked?
    
    # - a. Checking the whole list to get the trend
    isIncreasing = reportTrend( report )
    
    if isIncreasing is None:
        return False # In case we have a nullifying trend
    
    
    # - b. Checking the trend for the whole list now (we stop at the n-1 element)!
    for i in range( len(report[:-1]) ):
        
        # Value not INCREASING properly
        if  ( ( isIncreasing ) and ( report[i] >= report[i+1] ) ):
            isRuleChecked = False
            break
        
        # Value not DECREASING properly
        elif( ( not(isIncreasing) ) and ( report[i] <= report[i+1] ) ):
            isRuleChecked = False
            break

    # - c. Let's report if the "report" is safe. ;)
    # If there was an error detected:
    if( not(isRuleChecked) ):
        # print("[!] Rule #1: trend (increase/decrease) not respected . REPORT:", report)
        return False
    
    # Otherwise, we can keep going
    # print( "[OK] Rule #1. Report:", report )
    return True


def safetyCheckRule_2( report, minLevelDifference=1, maxLevelDifference=3 ):
    
    isRuleChecked = True # BOOLEAN: is the whole safety rule OK or not
    
    # - a. Checking for each level in the report (excluded the last one)
    for i in range( len(report[:-1]) ):
        
        value_1 = report[i]
        value_2 = report[i+1]
        
        if( not( minLevelDifference <= abs( value_2 - value_1 ) <= maxLevelDifference ) ):
            isRuleChecked = False
            break
    
    
    # - b. Once the whole report has been checked (or break), we state the rule check!
    if ( isRuleChecked ):
        # print( "[OK] Rule #2. Report:", report )
        return True
    
    else:
        # print("[!] Rule #2: difference out of bound. REPORT:", report)
        return False


def safetyCheck( report ):
    
    # -- 1. RULES: Trend & Level difference checks
    rule1_Check = safetyCheckRule_1( report )
    rule2_Check = safetyCheckRule_2( report )
    
    # -- 2. 
    if (rule1_Check) and (rule2_Check):
        return True
    
    else:
        return False


def dampenerRule_1( input_report ):
    isIncreasing = None             # BOOLEAN: Is the report increasing/decreasing?
    report = input_report.copy()    # Copying the original report before modifying it
    hasDampenerApplied = False      # BOOL: have we applied the dampering effect?
    
    # - a. Checking the whole list to get the trend
    isIncreasing = reportTrend( report )
    
    if isIncreasing is None:
        # In case we have a nullifying trend
        # We expect it to be unfixable.
        
        return report, hasDampenerApplied
    
    
    # - b. Now checking where the trend has been broken!
    #      And removing the element that got it wrong.
    
    if( not(hasDampenerApplied) ):
        
        for i in range( len(report[:-1]) ):
        
            # Value not INCREASING properly
            if  ( ( isIncreasing ) and ( report[i] >= report[i+1] ) ):
                report.pop(i+1)
                hasDampenerApplied = True
                break
            
            # Value not DECREASING properly
            elif( ( not(isIncreasing) ) and ( report[i] <= report[i+1] ) ):
                report.pop(i+1)
                hasDampenerApplied = True
                break
        
        # The dampener should have been applied now.
        # Let's just check in any cases:
        if( not(hasDampenerApplied) ):
            # print( "[ERROR] Somehow, the Dampener couldn't find the wrong element for rule #1. REPORT:", report)
            return report, hasDampenerApplied
        
    
    # Returning the dampened report.
    return report, hasDampenerApplied


def dampenerRule_2( input_report, minLevelDifference=1, maxLevelDifference=3  ):
    
    report = input_report.copy()
    hasDampenerApplied = False # BOOLEAN: have we applied the dampener?
    
    # - a. Checking for each level in the report (excluded the last one)
    for i in range( len(report[:-1]) ):
        
        value_1 = report[i]
        value_2 = report[i+1]
        
        if( not( minLevelDifference <= abs( value_2 - value_1 ) <= maxLevelDifference ) ):
            
            # If we found the wrong value, we pop it out!
            report.pop(i+1)
            hasDampenerApplied = True
            break
    
    # Then, once the whole list has been checked, we return the new list!
    
    # In case nothing has been applied:
    if( not(hasDampenerApplied) ):
        # print( "[ERROR] Somehow, the Dampener couldn't find the wrong element for rule #2. REPORT:", report)
        return report, hasDampenerApplied
        
    
    # Returning the dampened report.
    return report, hasDampenerApplied
    

def problemDampener( input_report ):
    
    hasDampened_Rule1 = False
    hasDampened_Rule2 = False 
    
    # Output list declaration
    damper_report = input_report.copy()
    
    # - a. Let's check if rule #1 is OK
    rule1_Check = safetyCheckRule_1( input_report )
    
    # If the rule is not OK, then we fix the wrong element once
    if( not(rule1_Check) ):
        damper_report,hasDampened_Rule1 = dampenerRule_1( input_report )
    
    # - b. If the rule #1 was OK, let's check for rule #2
    else:
        rule2_Check = safetyCheckRule_2( input_report )
        
        # Same here, if the rule wasn't checked, then it get fixed once!
        if( not(rule2_Check) ):
            damper_report,hasDampened_Rule2 = dampenerRule_2( input_report )
    
    
    # Global message (DEBUG)
    if( hasDampened_Rule1 ):
        print( "Dampening R1 applied. REPORT =", damper_report, ",with original =", input_report)
    
    if( hasDampened_Rule2 ):
        print( "Dampening R2 applied. REPORT =", damper_report, ",with original =", input_report)
    
    if( not(hasDampened_Rule1) and not(hasDampened_Rule2) ):
        print( "NO DAMPENING AT ALL. REPORT =", damper_report, "which should be =", input_report)
    
    # If any of the 2 rules weren't OK, a dampening has been applied once.
    # The report is ready to be used.

    return damper_report


# --- C. main.py

def main():
    # -- 1. File reading
    reports_data    = [] # This will hold all the reports, line by line
    report_buffer   = [] # This will be only used to construct the "reports" array

    with open("programs/2024/Python/02_Red-Nosed-Reports/sample.txt", "r") as input_file:
        
        for line in input_file:
            
            # Getting from "7 6 4 2 1\n" to "[7, 6, 4, 2, 1]":
            report_buffer = [int(value) for value in line.strip("\n").split(" ")]
            
            # Then saving the data in the global
            reports_data.append( report_buffer )
            
    # DEBUG: complete data
    # print( reports_data )


    # -- 2. Safe Report Count (SRC)

    safeReportCounter = int( 0 )

    for report in reports_data:
        
        # -- 3. Error Dampener
        # If any error is detected in the system, get ride of 1 level only.
        # Then, run the check execution as usual.
        
        if ( isDampenerActive ):
            originalReport = report.copy() # Make a backup of the report
            report = problemDampener( report ) # Set the new "report" as the fixed report
        
        
        # -- 4. Safety check
        isReportSafe = safetyCheck( report )
        
        if( isReportSafe ):
            safeReportCounter += 1
        
        # else:
            # print("REPORT:", report, "+ ORIGINAL:", originalReport)            

    # -- 5. Final display
    # Once we've analyzed all the reports, we can display the amount to the user!
    print( "Safe Reports (NB):", safeReportCounter, "\n" )

    # Additional informations
    print( "Additional stats:")
    print( "Total Reports (NB):", len(reports_data) )
    print( "% of valid reports:", round( safeReportCounter/len(reports_data)*100, 1), "%" )



# --- D. main() execution

main()