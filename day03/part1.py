total_score = 0

with open("puzzledata.txt") as file:
    for line in file.readlines():
        # get the two halves of the string
        line = line.strip()
        first_half = line[:(len(line) // 2)]
        second_half = line[(len(line) // 2):]

        # find matches in the two halves
        if any((match := item) in second_half for item in first_half):
            score = ord(match)
            if match.islower(): 
                score -= 96
            else: 
                score -= 38
            total_score += score

print(total_score)