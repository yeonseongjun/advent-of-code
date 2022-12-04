answer, counter, my_list = 0, 0, []
data = open("input.txt").read()
for line in data.split("\n"):
    counter += 1
    my_list.append(line)
    if counter != 3:
        continue
    common_letter_set = set(my_list[0]) & set(my_list[1]) & set(my_list[2])
    common_letter = common_letter_set.pop()
    if ord(common_letter) >= 97:
        answer += ord(common_letter) - 96
    else:
        answer += ord(common_letter) - 38
    counter, my_list = 0, []
print(answer)
    
