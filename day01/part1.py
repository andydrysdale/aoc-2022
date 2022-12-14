biggest_total = 0
running_total = 0

with open("puzzledata.txt") as file:
    for line in file.readlines():
        if line == "\n":
            if running_total > biggest_total: 
                biggest_total = running_total
            running_total = 0
        else:
            running_total += int(line)            

print(biggest_total)
