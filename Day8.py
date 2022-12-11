from typing import List


trees: List[str] = []

with open("Day8.txt") as f:
    trees = [l.rstrip("\n") for l in f]

def is_tree_visible(y, x):
    """PART 1"""
    tree_height = int(trees[y][x])

    ## LEFT
    is_visible = True
    for column in range(x-1, -1, -1):
        if int(trees[y][column]) >= tree_height:
            is_visible = False
    if is_visible:
        return True

    ## RIGHT
    is_visible = True
    for column in range(x+1, len(trees[y])):
        if int(trees[y][column]) >= tree_height:
            is_visible = False
    if is_visible:
        return True

    ## UP
    is_visible = True
    for row in range(y-1, -1, -1):
        if int(trees[row][x]) >= tree_height:
            is_visible = False
    if is_visible: return True

    ## DOWN
    is_visible = True
    for row in range(y+1, len(trees)):
        if int(trees[row][x]) >= tree_height:
            is_visible = False
    
    return is_visible


def calculate_scenic_score(y, x):
    """PART 2"""
    tree_height = int(trees[y][x])
    scenic_scores = [0, 0, 0, 0]

    ## LEFT
    for column in range(x-1, -1, -1):
        scenic_scores[0] = scenic_scores[0] + 1
        if int(trees[y][column]) >= tree_height:
            break

    ## RIGHT
    for column in range(x+1, len(trees[y])):
        scenic_scores[1] = scenic_scores[1] + 1
        if int(trees[y][column]) >= tree_height:
            break


    ## UP
    for row in range(y-1, -1, -1):
        scenic_scores[2] = scenic_scores[2] + 1
        if int(trees[row][x]) >= tree_height:
            break

    ## DOWN
    for row in range(y+1, len(trees)):
        scenic_scores[3] = scenic_scores[3] + 1
        if int(trees[row][x]) >= tree_height:
            break
    
    return scenic_scores


# the edges (rectangle perimeter) and subtract 4 to remove repeating corners
visible_trees = 2 * (len(trees) + len(trees[0])) - 4
tree_scenic_scores = []

for row in range(1, len(trees) - 1):
    for column in range(1, len(trees[row]) - 1):
        if is_tree_visible(row, column):
            visible_trees += 1
        tree_scenic_scores.append(calculate_scenic_score(row, column))

print(visible_trees)
print(max(map(lambda score: score[0] * score[1] * score[2] * score[3], tree_scenic_scores)))