strategy_list = []

with open("Day2.txt") as f:
    strategy_list = [line.rstrip() for line in f]

item_scores = {
    "X": 1, "A": 1,
    "Y": 2, "B": 2,
    "Z": 3, "C": 3
}
game_outcomes = [
    ['A Z', 'B X', 'C Y'], # you lost
    ['A X', 'B Y', 'C Z'], # you drew
    ['A Y', 'B Z', 'C X'] # you won
]


# Part 1
total_points_part1 = 0
for game in strategy_list:
    outcome = list(filter(lambda g: game in g[1] , enumerate(game_outcomes)))[0]
    total_points_part1 += item_scores[game[2]] + outcome[0] * 3

print(total_points_part1)

# Part 2
outcome_strategy_points = {
    "X": 0,
    "Y": 3,
    "Z": 6
}

# our strategy is related to shifting
# if we need to lose we shift right by two
# if we need to draw we don't shift
# if we need to win we shift right once
enemy_moves = ["A", "B", "C"]
strategy_shift = {
    "X": 2,
    "Y": 0,
    "Z": 1
}

total_points_part2 = 0
for game in strategy_list:
    enemy_move, my_strategy = game.split(" ")
    enemy_move_index = enemy_moves.index(enemy_move)
    my_move_index = (enemy_move_index + strategy_shift[my_strategy]) % len(enemy_moves)
    my_move = enemy_moves[my_move_index]
    total_points_part2 += outcome_strategy_points[game[2]] + item_scores[my_move]

print(total_points_part2)