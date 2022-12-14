score = 0 

with open("puzzledata.txt") as file:
    for line in file.readlines():
        match line.strip():
            case "A X": score += 3 #rock,scissors
            case "A Y": score += 4 #rock,rock
            case "A Z": score += 8 #rock,paper
            case "B X": score += 1 #paper,rock
            case "B Y": score += 5 #paper,paper
            case "B Z": score += 9 #paper,scissors
            case "C X": score += 2 #scissors,paper
            case "C Y": score += 6 #scissors,scissors
            case "C Z": score += 7 #scissors,rock

print(score)