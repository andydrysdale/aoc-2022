score = 0 

with open("puzzledata.txt") as file:
    for line in file.readlines():
        line = line.strip()

        # add score for my pick
        if line[2] == "X": score += 1
        if line[2] == "Y": score += 2 
        if line[2] == "Z": score += 3

        # add score for draw
        if line == "A X" or line == "B Y" or line == "C Z":
            score += 3
        # add score for win
        elif line == "A Y" or line == "B Z" or line == "C X":
            score += 6

print(score)