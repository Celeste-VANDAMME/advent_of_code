# ----- File reading
data_directory = "2015/05/data/input.txt"

with open(data_directory, "r") as data_file:
    input_data = data_file.read()

# Print the result:
# print( input_data )

# ----- Line analysis

niceLineCounter = 0

for line in input_data.split( "\n" ):
    
    # Loop initialization
    isLineNaughty = False
    
    # RULE-1 : Combinaison of 2 letters repeated accross the line
    isRule1_OK = False
    
    for i in range(len(line[:-3])):
        # 1. Find the combinaison
        twoLetterCombinaison = line[i] + line[i+1]
        
        # 2. Unraveling all the line to check if there are
        # new iteration of the same pattern.
        
        for j in range(len(line) - 1):
            if  j == i-1 or j == i or j == i+1:
                continue
            
            foundCombinaison = line[j] + line[j+1]
            
            if foundCombinaison == twoLetterCombinaison:
                isRule1_OK = True
                break
    
    if not(isRule1_OK):
        isLineNaughty = True
    
    
    # RULE-2 : Repeating through one (unknown) letter
    isRule2_OK = False
    
    for i in range(len(line[:-2])):
        if line[i] == line[i+2]:
            
            isRule2_OK = True
            break
    
    if not(isRule2_OK):
        isLineNaughty = True
    
    
    # RULES COMPILATION: Final check
    
    if not(isLineNaughty):
        
        # Extra layer of check:
        if isRule1_OK and isRule2_OK:
            niceLineCounter += 1
            print(line)

print( "#2 Nice line counter = ", niceLineCounter )