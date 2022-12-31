input_file = open("input-7.txt","r")
input_data = input_file.read()
terminal_lines = input_data.split("\n")

directories = {"/home":0}
path = "/home"

for line in terminal_lines:
    # setting current path
    if line[0:4] == "$ cd" and line != "$ cd ..":
        if line[5:6] == "/":
            path = "/home"
        else:
            current_directory = line[5:]
            path = path + "/" + current_directory
            directories.update({path:0})

    if line[0].isnumeric():
        # getting  file size
        file_size = int(line[:line.find(" ")])
        directory = path
        for i in range(path.count("/")):
            directories[directory] += file_size
            directory = directory[:directory.rfind("/")]

    if line == "$ cd ..":
        # setting directory we're currently in
        path = path[0:path.rfind("/")]


space_needed = 30_000_000
total_disk_space = 70_000_000
threshold = space_needed - (total_disk_space - directories["/home"])
sizes_above_threshold = []

part_1_result = 0
for directory, size in directories.items():
    # === PART 1 ===
    if size <= 100_000:
        part_1_result += size
    # === PART 2 ===
    if size >= threshold:
        sizes_above_threshold.append(size)

part_2_result = min(sizes_above_threshold)


print(f"Sum of directories with a total size of at most 100000: {part_1_result}")
print(f"Size of smallest directory that would free up enough space: {part_2_result}")