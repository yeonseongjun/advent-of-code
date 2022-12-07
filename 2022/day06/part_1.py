data = open("input.txt").read()
word = "" # abce
answer = 0
for index, letter in enumerate(data):
    word += letter
    if len(word) < 4:
        continue
    if len(set(word)) == len(word):
        answer = index + 1
        break
    else:
        word = word[1:]
print(answer)
