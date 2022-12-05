data = open("input.txt").read()
my_dict = {}
answer = ""
for line in data.split("\n"):
    if "[" in line:
        stack = 0
        space_counter = 0
        for container in line.split(' '):
            if container == '':
                space_counter += 1
                continue
            stack += 1 + int(space_counter / 4)
            space_counter = 0
            if stack in my_dict:
                my_dict[stack].insert(0, container[1])
            else:
                my_dict[stack] = [container[1]]
    if "move" in line:
        numbers = [int(num) for num in line.split() if num.isdigit()]
        new_list = my_dict[numbers[1]][-numbers[0]:]
        my_dict[numbers[2]].extend(new_list)
        del my_dict[numbers[1]][-numbers[0]:]

for num in range(len(my_dict)):
    answer += my_dict[num + 1].pop()
print(answer)