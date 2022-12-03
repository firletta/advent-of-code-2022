import os.path

try:
    file = open("input.txt","r")
except IOError:
    print("Error:\n'input.txt' was not found.")
    exit()

input_file = open("input.txt","r")
input_data = input_file.read()
input_lists = input_data.split("\n\n")
elves_calories_listed = []
elves_calories_sum = []

for i in input_lists:
    split = i.split("\n")
    calories_sum = 0
    for j in split:
        calories_sum += int(j)
    elves_calories_sum.append(calories_sum)
    elves_calories_listed.append(split)

winner = max(elves_calories_sum)


print(f"Elf number {elves_calories_sum.index(winner) + 1} has the most calories, which is: {winner}")