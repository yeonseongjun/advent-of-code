score = 0
my_dict = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
data = open("input.txt").read()
for line in data.split("\n"):
    opponent, result = my_dict[line[0]], my_dict[line[-1]]
    if result == 1:
        temp = opponent - 1 if opponent - 1 > 0 else 3
        score += temp

    if result == 2:
        score += 3 + opponent

    if result == 3:
        temp = opponent + 1 if opponent + 1 < 4 else 1
        score += 6 + temp

print(score)
        