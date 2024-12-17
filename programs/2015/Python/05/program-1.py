# ----- File reading
data_directory = "2015/05/data/input.txt"

data_file = open(data_directory, "r")
input_data = data_file.read()
data_file.close()

# Print the result:
# print( input_data )

# ----- Line analysis
niceLineCounter = 0
vowels = "aeiou"
forbiddenCombinaisons = ["ab", "cd", "pq", "xy"]

for line in input_data.split( "\n" ):
    
    isNaughty = False
    
    # RULE-1: >= 3 vowels
    isRULE1_ok = False
    vowelCounter = 0
    
    for character in line:
        if character in vowels:
            vowelCounter += 1
            
            if vowelCounter >= 3:
                isRULE1_ok = True
                break
    
    if not(isRULE1_ok):
        isNaughty = True
        
        
    # RULE-2: double appearing letter next to each other
    isRULE2_ok = False
    
    for i in range(len(line[:-1])):
        # Check if the NEXT element is equal
        if(line[i] == line[i+1]):
            isRULE2_ok = True
            break
    
    if not(isRULE2_ok):
        isNaughty = True
    
    
    # RULE-3: not containing specific strings
    isRULE3_ok = False
    isForbiddenTriggered = False
    
    for prohibitedCombinaison in forbiddenCombinaisons:
        
        # Check whether one combinaison is found
        if prohibitedCombinaison in line:
            isForbiddenTriggered = True
            break
    
    if isForbiddenTriggered:
        isNaughty = True
    
    else:
        isRULE3_ok = True
    
    
    # ~~~ Final check
    if not(isNaughty):
        
        # Extra check here (unnecessary):
        if isRULE1_ok & isRULE2_ok & isRULE3_ok:
            niceLineCounter += 1

print('1# "Nice" lines: ', niceLineCounter )