count = 0
with open("puzzledata.txt") as file:
    for line in file.readlines():
        # split each line read into a list of four integers
        parts = [int(i) for i in line[:-1].replace("-", ",").split(",")]

        # if the lower or upper limits of either pair exist in the  
        # range of the other pair, increment the count
        if any([parts[2] <= parts[0] <= parts[3], 
                parts[2] <= parts[1] <= parts[3], 
                parts[0] <= parts[2] <= parts[1], 
                parts[0] <= parts[3] <= parts[1]]): 
            count += 1
 
print(count)
