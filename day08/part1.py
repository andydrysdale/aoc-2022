trees = []
hidden_trees = []

with open("puzzledata.txt") as file:
    for line in file.readlines():
        trees.append([int(i) for i in list(line[:-1])])

width = len(trees[0])
height = len(trees)

for y in range(1, height - 1):
    for x in range(1, width - 1):
        tree_height = trees[y][x]

        # check if visible from left
        hidden_left = False
        for i in range(x):
            if trees[y][i] >= tree_height: hidden_left = True
        
        # check if visible from right
        hidden_right = False
        for i in range(x+1, width):
            if trees[y][i] >= tree_height: hidden_right = True

        # check if visible from top
        hidden_top = False
        for i in range(y):
              if trees[i][x] >= tree_height: hidden_top = True

        # check if visible from bottom
        hidden_bottom = False
        for i in range(y+1, height):
            if trees[i][x] >= tree_height: hidden_bottom = True

        if hidden_left and hidden_right and hidden_top and hidden_bottom:
            hidden_trees.append((y, x))

# draw the forest, visible = green, hidden = grey
for y in range(height):
    for x in range(width):
        if (y, x) in hidden_trees:
            print(f"\033[30m{trees[y][x]}", end="")
        else:
            print(f"\033[32m{trees[y][x]}", end="")
    print("")     

visible_count = (width * height) - len(hidden_trees)
print(f"\033[00mVisible trees: {visible_count}")