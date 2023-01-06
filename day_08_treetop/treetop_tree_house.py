input_file = open("input-8.txt","r")
input_data = input_file.read()
forest = input_data.split("\n")

hidden_trees = 0

for i in range(0,99):
    for j in range(0,99):
        current_tree = forest[i][j]
        hidden = []
        if i == 0 or i == 98:
            pass
        if j == 0 or j == 98:
            pass

        top = forest[0:i-1]
        bottom = forest[i+1:98]
        left = []
        right = []
        for k in range(0,i-1):
            left.append(forest[k][j])
        for l in range(i+1,98):
            right.append(forest[l][j])

        for tree in top:
            if tree >= current_tree:
                hidden.append("top")
                break
        for tree in bottom:
            if tree >= current_tree:
                hidden.append("bottom")
                break
        for tree in left:
            if tree >= current_tree:
                hidden.append("left")
                break
        for tree in right:
            if tree >= current_tree:
                hidden.append("right")
                break
        if len(hidden) == 4:
            hidden_trees += 1

all_trees = 99 * 99
visible_trees = all_trees - hidden_trees


print(visible_trees)









