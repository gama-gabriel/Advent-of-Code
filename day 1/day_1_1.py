with open("day 1/day_1_input.txt", 'r') as file:
    content = file.readlines()
    current = 0
    biggest = 0
    for line in content:
        if current > biggest:
            biggest = current
        if line == '\n':
            current = 0
            continue
        current += int(line.split("\n")[0])

print(biggest)