# -------------------
# ADVENT OF CODE
#       2024
#
# Link:
# https://adventofcode.com/2024/day/1
# 
# Program:
#   #1-A + #1-B
# 
# Program title:
#   Historian Hysteria
#
# DEV:
#   - Celeste VANDAMME
#       GitHub: https://github.com/Celeste-VANDAMME
#       Discord: @slak3r
#
# -------------------

# --- 1. File opening
with open("programs/2024/Python/01_Historian-Hysteria/input.txt", "r") as input_file:


    # --- 2. 2 arrays creation

    # Goal: fill these arrays
    first_numbers   = []
    second_numbers  = []
    distance        = []

    for line in input_file:

        line_values = line.split( "   " )
        number_1 = int(line_values[0])
        number_2 = int(line_values[1][:-1])
        
        
        first_numbers.append( number_1 )
        second_numbers.append( number_2 )
        
         
# 3. We need to sort the arrays from smallest to biggest
first_numbers.sort()
second_numbers.sort()


# --- DISTANCE CALCULATION

# 4. We calculate on the go the distance between each element
for number_1, number_2 in zip(first_numbers, second_numbers):
    distance.append(abs(number_1 - number_2))


# 5. We get the total distance of the list!
distance_total = sum( distance )

print( "The total distance of the input is:", distance_total, "(int)" )


# --- SIMILARITY SCORE CALCULATION

similarityScore = int( 0 )

# 6. For each number in the first list (number #1)...
for number_1 in first_numbers:
    
    # We want to check how many time it appears on the second list (number #2)!    
    for number_2 in second_numbers:
        
        if( number_1 == number_2 ):
            # And if it's a match, we then add the number into the matching system. :)
            similarityScore += number_1
        

# 7. We found the similarity:
print( "The similarity of the two lists is:", similarityScore, "(int)" )
