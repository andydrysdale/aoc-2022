terminal = []
all_files = {}
directories = { "": 0 }

# read the sections of each terminal line into a list of lists
with open("puzzledata.txt") as file:
    for line in file.readlines(): terminal.append(line[:-1].split())

# iterate through all the terminal lines
current_path = ""
for line in terminal[1:]:
    # if the line is a 'cd' command, alter the current path accordingly
    if line[0] == "$":
        if line[1] == "cd":
            if line[2] == "..":
                current_path = "/".join(current_path.split("/")[:-1])
            else: 
                current_path = current_path + "/" + line[2]
    # if not a command, must be part of a directory listing. Build a 
    # dictionary of all files with their sizes (0 for directories), and
    # build a second dictionary of just the directories initialised to -1
    else:
        key = current_path + "/" + line[1]
        if line[0] == "dir":
            directories[key] = -1
            value = 0
        else:
            value = int(line[0])
        all_files[key] = value

# go through the directory dictionary and make the value 
# the sum of all files that start with that directory 
for dir_key, dir_value in directories.items():
    size = 0
    for files_key, files_value in all_files.items():
        if files_key.startswith(dir_key + "/"): 
            size += files_value
    directories[dir_key] = size

# add up all the directories over 100k
total = 0
for key, value in directories.items():
    if value <= 100_000: total += value

print(total)
