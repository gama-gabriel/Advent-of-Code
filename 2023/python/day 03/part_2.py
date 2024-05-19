def check(start, end, y, number):
    directions = {'u': [-1, 0], 'ru': [-1, 1], 'lu': [-1, -1], 'd': [1, 0], 'rd': [1, 1], 'ld': [1, -1], 'l': [0, -1], 'r': [0, 1] }
    cant_go = ''
    global lines
    global gears

    if start == 0:
        cant_go += 'l'
    if end == len(lines[y]) - 1:
        cant_go += 'r'
    if y == 0:
        cant_go += 'u'
    if y == len(lines) - 1:
        cant_go += 'd'
        
    for x in range(start, end):
        for direction, add in directions.items():
            add_y, add_x = add
            new_y = y + add_y
            new_x = x + add_x
            if direction[0] in cant_go or direction[-1] in cant_go:
                continue
            curr = lines[new_y][new_x]
            
            if curr == '*':
                if f'{new_y} {new_x}' in gears.keys():
                    gears[f'{new_y} {new_x}'].append(int(number))
                else:
                    gears[f'{new_y} {new_x}'] = [int(number)]
                return

lines = open('input.txt', 'r').readlines()
number = ''
y = 0
x = 0
result = 0
gears = {}

while y < len(lines):
    while x < len(lines[y]):
        if lines[y][x].isnumeric():
            while lines[y][x].isnumeric():
                number += lines[y][x]
                if len(number) == 1:
                    start = x
                x += 1

            end = x
            check(start, end, y, number)
            number = ''
        else:
            x += 1
    y += 1
    x = 0

for item in gears.values():
    if len(item) == 2:
        result += item[0] * item[1]

print(result)
