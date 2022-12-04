answer = 0
data = open("input.txt").read()
for line in data.split("\n"):
    mid = int(len(line) / 2)
    first, second = line[:mid], line[mid:]
    common_letter_set = set(first) & set(second)
    common_letter = common_letter_set.pop()
    if ord(common_letter) >= 97:
        answer += ord(common_letter) - 96
    else:
        answer += ord(common_letter) - 38
print(answer)