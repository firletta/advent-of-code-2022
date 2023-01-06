import numpy as np

with open('input-8.txt', 'r') as f:
    tree_lines = f.readlines()
    tree_lines = [line.strip() for line in tree_lines]

trees = np.zeros((len(tree_lines), len(tree_lines[0])), dtype=int)
for i, line in enumerate(tree_lines):
    trees[i, :] = np.array(list(line))

# the edges are always visible
visible_trees = 2*len(tree_lines[0]) + 2 *(len(tree_lines)-2)

# iterate over trees
for i in range(1, trees.shape[0]-1):
    for j in range(1, trees.shape[1]-1):
        tree_column = trees[:, j] - trees[i, j]
        tree_row = trees[i, :] - trees[i, j]
        routes = [tree_row[:j], tree_row[j+1:], tree_column[:i], tree_column[i+1:]]
        if sum(list(map(lambda route: (route<0).all(), routes))) > 0:
            visible_trees += 1

print("Part 1:", visible_trees)

# https://galaxyinferno.com/how-to-solve-advent-of-code-2022-day-8-with-python/
# https://painted-brush-a63.notion.site/day-8-O-n-with-next-greater-element-algorithm-ce3fb66663be44aea022ba1731fbe33b







