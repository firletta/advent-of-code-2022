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

first_place = max(elves_calories_sum)

# print(f"Elf number {elves_calories_sum.index(first_place) + 1} has the most calories, which is: {first_place}")

elves_calories_sum.remove(first_place)
second_place = max(elves_calories_sum)
elves_calories_sum.remove(second_place)
third_place = max(elves_calories_sum)

top_three = first_place + second_place + third_place
print(first_place, second_place, third_place)
print(top_three)