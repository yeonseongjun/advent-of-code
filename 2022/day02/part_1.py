score = 0
my_dict = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
data = open("input.txt").read()
for line in data.split("\n"):
    opponent, my_choice = my_dict[line[0]], my_dict[line[-1]]
    score += my_choice
    if opponent == my_choice:
        score += 3
    if my_choice + opponent == 4 and my_choice - opponent < 0:
            score += 6
    elif my_choice - opponent > 0:
        score += 6
print(score) 
