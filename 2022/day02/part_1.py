score = 0
my_dict = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
data = open("input.txt").read()
for line in data.split("\n"):
    opponent, me = my_dict[line[0]], my_dict[line[-1]]
    score += me
    if opponent == me:
        score += 3
    if me + opponent == 4 and me - opponent < 0:
            score += 6
    elif me - opponent > 0:
        score += 6
print(score) 
