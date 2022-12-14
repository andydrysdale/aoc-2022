count = 0
with open("puzzledata.txt") as file:
    for line in file.readlines():
        # split each line read into a list of four integers
        parts = [int(i) for i in line[:-1].replace("-", ",").split(",")]

        # if the range of either pair exists entirely inside the range of the other pair, increment the count
        if (parts[0] >= parts[2] and parts[1] <= parts[3]) or (parts[2] >= parts[0] and parts[3] <= parts[1]): count += 1     

print(count)
