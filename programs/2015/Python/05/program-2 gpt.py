# ----- File reading
data_directory = "2015/05/data/input.txt"

with open(data_directory, "r") as data_file:
    input_data = data_file.read()

# Print the result:
# print( input_data )

# ----- Line analysis

def contains_repeated_pair(string):
    for i in range(len(string) - 1):
        pair = string[i:i+2]
        if string.count(pair) >= 2:
            return True
    return False

def contains_repeat_with_one_between(string):
    for i in range(len(string) - 2):
        if string[i] == string[i+2]:
            return True
    return False

def is_nice(string):
    return contains_repeated_pair(string) and contains_repeat_with_one_between(string)

def count_nice_strings(strings):
    nice_count = 0
    for string in strings:
        if is_nice(string):
            nice_count += 1
            print(string)
    return nice_count

data_directory = "2015/05/data/input.txt"

with open(data_directory, "r") as data_file:
    input_data = data_file.read().splitlines()

nice_count = count_nice_strings(input_data)
print("Number of nice strings:", nice_count)