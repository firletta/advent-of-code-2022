input_file = open("input-2.txt","r")
input_data = input_file.read()
data = input_data.split("\n")

points = 0

# part 1
for i in data:
    if i[0] == 'A':
        if i[2] == 'X':
            points += 1 + 3
        elif i[2] == 'Y':
            points += 2 + 6
        elif i[2] == 'Z':
            points += 3
    if i[0] == 'B':
        if i[2] == 'X':
            points += 1
        elif i[2] == 'Y':
            points += 2 + 3
        elif i[2] == 'Z':
            points += 3 + 6
    if i[0] == 'C':
        if i[2] == 'X':
            points += 1 + 6
        elif i[2] == 'Y':
            points += 2
        elif i[2] == 'Z':
            points += 3 + 3

print("1st strategy:",points)

# part 2 - X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
# rock - 1, paper - 2, scissors - 3
points_new = 0

for i in data:
    if i[0] == 'A':
        if i[2] == 'X':
            points_new += 3
        elif i[2] == 'Y':
            points_new += 1 + 3
        elif i[2] == 'Z':
            points_new += 2 + 6
    if i[0] == 'B':
        if i[2] == 'X':
            points_new += 1
        elif i[2] == 'Y':
            points_new += 2 + 3
        elif i[2] == 'Z':
            points_new += 3 + 6
    if i[0] == 'C':
        if i[2] == 'X':
            points_new += 2
        elif i[2] == 'Y':
            points_new += 3 + 3
        elif i[2] == 'Z':
            points_new += 1 + 6

print("2nd strategy",points_new)

