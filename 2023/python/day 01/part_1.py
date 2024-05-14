lines = open('input.txt', 'r').readlines()
result = 0
number = ''

for line in lines:
    for i in range(0, len(line)):
        char = line[i]
        if char.isnumeric():
            number += char
            break

    for i in range(len(line) - 1, -1, -1):
        char = line[i]
        if char.isnumeric():
            number += char
            break

    result += int(number)
    number = ''

print(result)
