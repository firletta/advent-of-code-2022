# 2022 Advent of Code Day 1
from os import read

# Read calorie inventory file.
with open("input.txt") as f:
    data = f.read()
f.close()

# Format data to integers.
data = data.splitlines()

for i in range(0,len(data)):
    if data[i] == "":
        data[i] = 0
    else:
        data[i] = int(data[i])

# Initialize variables.
calorie_count = 0
elf_inventory = []
elf = 0

# Part 1 - Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
for inv in range(0,len(data)):
    if data[inv] > 0:
        calorie_count += data[inv] # Add successive calorie numbers until next elf.
    else:
        elf_inventory.append(calorie_count) # Add elf x's inventory to the inventory array.
        calorie_count = 0 # Reset elf calorie count to 0.
        elf += 1 # Next elf.

print("Sum of calories for the top elf: %d" %max(elf_inventory))

# Part 2 - Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
elf_inventory = sorted(elf_inventory, reverse=True) # Sort inventory descending order.
print("Sum of calories for top three elves: %d" %sum(elf_inventory[0:3])) # Sum top 3 elves.