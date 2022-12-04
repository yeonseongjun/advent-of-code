ans = 0
data = open("input.txt").read()
for line in data.split("\n"):
    first, second = line.split(',')
    first_start, first_end = first.split("-")
    second_start, second_end = second.split("-")
    first_list = [num for num in range(int(first_start), int(first_end) + 1)]
    second_list = [num for num in range(int(second_start), int(second_end) + 1)]
    
    first_check = any([num in second_list for num in first_list])
    second_check = any([num in first_list for num in second_list])

    if first_check or second_check:
        ans += 1
    
print(ans)
    