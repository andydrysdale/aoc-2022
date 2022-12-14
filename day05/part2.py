tower_lines = []
instruction_lines = []
in_header = True

# Read the file into two lists of lines - one desctribing the starting 
# state of the tower and one with the move instructions
with open("puzzledata.txt") as file:
    for line in file.readlines():
        if line == "\n":
            in_header = False
        else:
            if in_header:
                tower_lines.append(line[:-1])
            else:
                instruction_lines.append(line[:-1])

# Work out the number of towers from the last line of the section describing the 
# tower. Then create a list of empty lists each representing a tower.
no_of_towers = int(tower_lines[-1][-2])
towers = [ [] for _ in range(no_of_towers) ]

# Read back up the tower description list, building the lists from bottom to top
for row in range(len(tower_lines) -2, -1, -1):
    for tower in range(no_of_towers):
        letter = tower_lines[row][(tower * 4) + 1]
        if letter != " ": towers[tower].append(letter)

# Apply the box moving instructions. The boxes are transferred via an intermediate stack
# stack to give the same outcome as if several were picked up at once
for line in instruction_lines:
    instruction = [int(i) for i in line.replace("move", "").replace("from", "").replace("to", "").split()]
    intermediate_stack = []
    for step in range(instruction[0]):
        intermediate_stack.append(towers[instruction[1] - 1].pop())
    for step in range(instruction[0]):
        towers[instruction[2] - 1].append(intermediate_stack.pop())
        
# Build a string representing the tower tops
tower_tops = ""
for i in range(no_of_towers):
    tower_tops += towers[i].pop()
print(tower_tops)