elf_calories, current_sum = [], 0
data = open("input.txt").read()

for line in data.split("\n"):
    if line:
        current_sum += int(line)
    else:
        elf_calories.append(current_sum)
        current_sum = 0

elf_calories.sort()
part_1 = elf_calories[-1]
part_2 = (sum(elf_calories[-3:]))

print(part_1)
print(part_2)
