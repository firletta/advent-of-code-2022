input_file = open("input-5.txt","r")
input_data = input_file.read()
supplies, instructions = input_data.split("\n\n")
supplies, instructions = supplies.splitlines(), instructions.splitlines()

stacks = [""] * 9

for i in range(len(supplies)-2,-1,-1):
    for j in range(1,len(supplies[0]), 4):
        if supplies[i][j].isupper() : stacks[j//4] += supplies[i][j]

# part 1
for i in instructions:
    a, b, c, d, e, f = i.split()
    crates_to_move, initial_stack, final_stack = int(b), int(d), int(f)
    initial_stack, final_stack = initial_stack - 1, final_stack - 1
    for j in range(crates_to_move):
        stacks[final_stack] += stacks[initial_stack][-1]
        stacks[initial_stack] = stacks[initial_stack][:-1]

top_crates_9000 = "CrateMover 9000's top crates: "
for i in stacks:
    top_crates_9000 += i[-1]

print(top_crates_9000)



