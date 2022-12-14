import string
datastream = ""

# Read the puzzle input
with open("puzzledata.txt") as file:
    datastream = file.readline()

# Iterate through the string checking for duplicates in a sliding window
for i in range(4, len(datastream)):
    # Grab the window to check as a list
    window = [j for j in datastream[i-4:i]]

    # Count the occurences of each letter in the string
    char_count = {}
    for char in string.ascii_lowercase: char_count[char] = 0
    for char in window: char_count[char] += 1

    # Check if any letter has more than one occurance...
    duplicate_found = False
    for j in char_count: 
        if(char_count[j] > 1):duplicate_found = True

    #...if not, output the index of the window and quit    
    if not duplicate_found: 
        print(i)
        exit(0)
    