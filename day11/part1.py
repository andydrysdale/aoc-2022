monkeys = []

class Monkey:
    # initialise the monkey with the passed variables and start a counter for inspections
    def __init__(self, items, operation, divisible_test, true_throw, false_throw):
        self.items = items
        self.operation = operation
        self.divisible_test = divisible_test
        self.true_throw = true_throw
        self.false_throw = false_throw
        self.inspection_count = 0

    # processes the items as the instuctions and returns a list of tuples describing 
    # what should be thrown to what monkey (i.e. monkey index and worry level)
    def process_items(self):
        items_to_throw = []
        for old in self.items:
            self.inspection_count += 1
            worry = eval(self.operation) // 3
            if worry % self.divisible_test == 0:
                items_to_throw.append((self.true_throw, worry))
            else:
                items_to_throw.append((self.false_throw, worry))
        self.items.clear()
        return(items_to_throw)


if __name__ == "__main__":
    # Read in the monkey descriptions and parse the attributes
    with open("puzzledata.txt") as file:
        for monkey_description in file.read().split("\n\n"):
            for line in monkey_description.splitlines():
                line = line.strip()
                if line.startswith("Starting items:"):
                    items = ([int(i) for i in line[16:].split(",")])
                elif line.startswith("Operation:"):
                    operation = line[17:]
                elif line.startswith("Test:"):
                    divisible_test = int(line[18:])
                elif line.startswith("If true:"):
                    true_throw = int(line[25:])
                elif line.startswith("If false:"):
                    false_throw = int(line[26:])

            # put a monkey object in the list of monkeys
            monkeys.append(Monkey(items, operation, divisible_test, true_throw, false_throw))
    
    # iterate through every monkey in turn for 20 rounds
    for round in range(20):
        for monkey in monkeys:
            # call the method to process the monkey's items and append 
            # the other monkeys' item lists based on what is thrown where
            for throw in monkey.process_items():
                monkeys[throw[0]].items.append(throw[1])

    # put the inspection counts in a list then calculate the 
    # monkey business from the highest two values in that list
    inspection_counts = []
    for monkey in monkeys: inspection_counts.append(monkey.inspection_count)
    inspection_counts.sort(reverse=True)
    print(inspection_counts[0] * inspection_counts[1])
    