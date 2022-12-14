history = [1]
register = 1

with open("puzzledata.txt") as file:
    for line in file.readlines():
        line_parts = line.split()
        match line_parts[0]:
            case "noop":
                history.append(register)
            case "addx":
                history.append(register)
                history.append(register)
                register += int(line_parts[1])

for y in range(6):
    for x in range(40):
        if (x - 1) <= history[(y * 40) + x + 1] <= (x + 1):
            print("#", end="")
        else:
            print(" ", end="")
    print("")
