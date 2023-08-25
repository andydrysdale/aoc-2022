knots = []
locations = [(0,0)]
KNOT_COUNT = 10

# takes the difference between the head and the tail and returns 
# where the tail should move relative to its current position
def get_follower_move(difference):
    match difference:
        case (2, 2):   return (1, 1)
        case (2, -2):  return (1, -1)
        case (-2, 2):  return (-1, 1)
        case (-2, -2): return (-1, -1)
        case (2, y):   return (1, y)   
        case (-2, y):  return (-1, y)          
        case (x, 2):   return (x, 1)   
        case (x, -2):  return (x, -1)   
        case _:        return (0, 0)    

if __name__ == "__main__":
    for i in range(KNOT_COUNT):
        knots.append((0,0))

    with open("puzzledata.txt") as file:
        for line in file.readlines():
            direction = line.split()[0]
            steps = int(line.split()[1])
            
            for s in range(steps):
                # move the head
                match direction:
                    case "U": knots[0] = (knots[0][0], knots[0][1] + 1)
                    case "D": knots[0] = (knots[0][0], knots[0][1] - 1)
                    case "L": knots[0] = (knots[0][0] - 1, knots[0][1])
                    case "R": knots[0] = (knots[0][0] + 1, knots[0][1])

                # move the following knots
                for k in range(1, KNOT_COUNT):
                    relative_follower_pos = get_follower_move((knots[k-1][0] - knots[k][0], knots[k-1][1] - knots[k][1]))
                    knots[k] = ((knots[k][0] + relative_follower_pos[0], knots[k][1] + relative_follower_pos[1]))

                # if the tail is in a new location add it to the list of locations
                if knots[KNOT_COUNT - 1] not in locations: locations.append(knots[KNOT_COUNT - 1])

    print(len(locations))
