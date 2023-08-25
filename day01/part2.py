running_total = 0
totals = []

with open("puzzledata.txt") as file:
    for line in file.readlines():
        if line == "\n":
            totals.append(running_total)
            running_total = 0
        else:
            running_total += int(line)

totals.sort(reverse=True)
print(totals[0] + totals[1] + totals[2])

