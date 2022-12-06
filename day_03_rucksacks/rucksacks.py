input_file = open("input-3.txt","r")
input_data = input_file.read()
data = input_data.split("\n")

priorities = []

for rucksack in data:
    compartment_1 = set(rucksack[:len(rucksack)//2])
    compartment_2 = set(rucksack[len(rucksack)//2:])
    for item in compartment_1:
        if item in compartment_2:
            if item.isupper():
                priorities.append(ord(item) - 38)
            else:
                priorities.append(ord(item) - 96)

print("1. Sum of priorities:", sum(priorities))

elf_groups = []
group_priorities = []

for elf in range(0, len(data), 3):
    elf_group = list(data[elf:elf + 3])
    elf_groups.append(elf_group)

for group in elf_groups:
    elf_1 = set(group[0])
    elf_2 = set(group[1])
    elf_3 = set(group[2])
    for item in elf_1:
        if (item in elf_2) and (item in elf_3):
            if item.isupper():
                group_priorities.append(ord(item) - 38)
            else:
                group_priorities.append(ord(item) - 96)

print("2. Sum of group priorities:", sum(group_priorities))




