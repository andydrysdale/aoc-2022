running_total = 0
backpacks = []

with open("puzzledata.txt") as file:
    for line in file.readlines():
        line = line.strip()

        # build a list of items in the backpack by number
        backpack_items = []
        for i in line:
            item_number = ord(i)
            if i.islower(): 
                item_number -= 96
            else:
                item_number -= 38
            backpack_items.append(item_number)

        # add this backpack contents list to the list of backpacks
        backpacks.append(backpack_items)

# go though the list of backpacks 3 at a time
for i in range(0, len(backpacks), 3):
    # make each backpack list a set
    first_elf = set(backpacks[i])
    second_elf = set(backpacks[i + 1])
    third_elf = set(backpacks[i + 2])

    # find the common item across 3 sets and add its value to to the running total
    running_total += (first_elf & second_elf & third_elf).pop()

print(running_total)