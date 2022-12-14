trees = []
hidden_trees = []
best_scenic_score = -1
best_scenic_score_location = (-1,-1)

with open("puzzledata.txt") as file:
    for line in file.readlines():
        trees.append([int(i) for i in list(line[:-1])])

width = len(trees[0])
height = len(trees)

for y in range(1, height - 1):
    for x in range(1, width - 1):
        tree_height = trees[y][x]

        # check left
        hidden_left = False
        trees_left = 0
        for i in range(x-1, -1, -1):
            trees_left += 1
            if trees[y][i] >= tree_height: 
                hidden_left = True
                break
        
        # check right
        hidden_right = False
        trees_right = 0
        for i in range(x+1, width):
            trees_right += 1
            if trees[y][i] >= tree_height: 
                hidden_right = True
                break

        # check top
        hidden_top = False
        trees_top = 0
        for i in range(y-1, -1, -1):
            trees_top += 1
            if trees[i][x] >= tree_height: 
                hidden_top = True
                break

        # check bottom
        hidden_bottom = False
        trees_bottom = 0
        for i in range(y+1, height):
            trees_bottom += 1
            if trees[i][x] >= tree_height:
                hidden_bottom = True
                break
        
        # calculate scenic score and see if it's the best so far
        scenic_score = trees_left * trees_right * trees_top * trees_bottom
        if scenic_score > best_scenic_score:
            best_scenic_score = scenic_score
            best_scenic_score_location = (y,x)

        if hidden_left and hidden_right and hidden_top and hidden_bottom:
            hidden_trees.append((y, x))

# draw the forest, visible = green, hidden = grey, most scenic = red
for y in range(height):
    for x in range(width):
        if (y, x) == best_scenic_score_location:
            print(f"\033[31m{trees[y][x]}", end="")
        elif (y, x) in hidden_trees:
            print(f"\033[30m{trees[y][x]}", end="")
        else:
            print(f"\033[32m{trees[y][x]}", end="")
    print("")     

visible_count = (width * height) - len(hidden_trees)
print(f"\033[00m    Visible trees: {visible_count}")
print("Best scenic score:", best_scenic_score)