head_pos = (0,0)
tail_pos = (0,0)
locations = [(0,0)]

# takes the difference between the head and the tail and returns 
# where the tail should move relative to its current position
def get_tail_move(difference):
    match difference:
        case (2, y):  return (1, y)   
        case (-2, y): return (-1, y)          
        case (x, 2):  return (x, 1)   
        case (x, -2): return (x, -1)   
        case _:       return (0, 0)    

if __name__ == "__main__":
    with open("puzzledata.txt") as file:
        for line in file.readlines():
            direction = line.split()[0]
            steps = int(line.split()[1])
            
            for i in range(steps):
                # move the head
                match direction:
                    case "U": head_pos = (head_pos[0],head_pos[1]+1)
                    case "D": head_pos = (head_pos[0],head_pos[1]-1)
                    case "L": head_pos = (head_pos[0]-1,head_pos[1])
                    case "R": head_pos = (head_pos[0]+1,head_pos[1])

                # move the tail 
                relative_tail_pos = get_tail_move((head_pos[0] - tail_pos[0], head_pos[1] - tail_pos[1]))
                tail_pos = ((tail_pos[0] + relative_tail_pos[0], tail_pos[1] + relative_tail_pos[1]))

                # if the tail is in a new location add it to the list of locations
                if tail_pos not in locations: locations.append(tail_pos)

    print(len(locations))
                