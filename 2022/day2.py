import os

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f"{dir_path}/day2_input.txt") as file:
    data = file.read()
    guide = data.split("\n")
    guide_tuples = []
    for line in guide:
        guide_tuples.append(tuple(line.split(" ")))

points_map = {
    'A': {'X': 1+3, 'Y': 2+6, 'Z': 3+0},
    'B': {'X': 1+0, 'Y': 2+3, 'Z': 3+6},
    'C': {'X': 1+6, 'Y': 2+0, 'Z': 3+3}
}

outcome_map = {
    'A': {'X': 'Z', 'Y': 'X', 'Z': 'Y'},
    'B': {'X': 'X', 'Y': 'Y', 'Z': 'Z'},
    'C': {'X': 'Y', 'Y': 'Z', 'Z': 'X'}
}

score = 0
for opponent, me in guide_tuples:
    my_play = outcome_map[opponent][me]
    score += points_map[opponent][my_play]

print(score)
