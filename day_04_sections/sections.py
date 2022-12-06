input_file = open("input-4.txt","r")
input_data = input_file.read()
data = input_data.split("\n")

elves_sections = []

for i in data:
    elves_pair = i.split(",")
    elves_pair_list = []
    for j in elves_pair:
        elfs_section = j.split("-")
        for k in elfs_section:
            k = int(k)
        elves_pair_list.append(elfs_section)
    elves_sections.append(elves_pair_list)

fully_contains_counter = 0

for pair in elves_sections:
    elf_1_start = int(pair[0][0])
    elf_1_end = int(pair[0][1])
    elf_2_start = int(pair[1][0])
    elf_2_end = int(pair[1][1])
    if (elf_1_start <= elf_2_start <= elf_2_end <= elf_1_end):
        fully_contains_counter += 1
    elif (elf_2_start <= elf_1_start <= elf_1_end <=  elf_2_end):
        fully_contains_counter += 1

print("Number of pairs where one range fully contain the other:", fully_contains_counter)

overlaps_counter = 0

for pair in elves_sections:
    elf_1_start = int(pair[0][0])
    elf_1_end = int(pair[0][1])
    elf_2_start = int(pair[1][0])
    elf_2_end = int(pair[1][1])
    temp_counter = 0
    for section in range(elf_1_start,elf_1_end + 1):
        if section in range(elf_2_start,elf_2_end + 1):
            temp_counter += 1
    if temp_counter > 0:
        overlaps_counter += 1

print("Number of overlaps:", overlaps_counter)
    





