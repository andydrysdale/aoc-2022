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

signal_strength = 0
for i in range(20,222,40):
    signal_strength += history[i] * i

print(signal_strength)
