lines = open('input.txt', 'r').readlines()
result = 0
number = ''
current = ''
keys = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', }

for line in lines:
    for i in range(0, len(line)):
        char = line[i]
        if char.isnumeric():
            number += char
            break

        current += char
        correct = [number for number in keys.keys() if number in current]
        if correct:
            number += keys[correct[0]]
            current = ''
            break

    for i in range(len(line) - 1, -1, -1):
        char = line[i]
        if char.isnumeric():
            number += char
            break

        current += char
        correct = [number for number in keys.keys() if number in current[::-1]]
        if correct:
            number += keys[correct[0]]
            current = ''
            break
        
    result += int(number)
    number = ''

print(result)
