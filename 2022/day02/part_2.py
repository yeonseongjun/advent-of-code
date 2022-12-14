score = 0
my_dict = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
data = open("input.txt").read()
for line in data.split("\n"):
    opponent, result = my_dict[line[0]], line[-1]
    if result == 'X':
        my_choice = opponent - 1 if opponent - 1 > 0 else 3
        score += my_choice
    if result == 'Y':
        score += 3 + opponent
    if result == 'Z':
        my_choice = opponent + 1 if opponent + 1 < 4 else 1
        score += 6 + my_choice
print(score)
