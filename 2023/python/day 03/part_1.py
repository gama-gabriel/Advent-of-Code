def check(start, end, y):
    directions = {'u': [-1, 0], 'ru': [-1, 1], 'lu': [-1, -1], 'd': [1, 0], 'rd': [1, 1], 'ld': [1, -1], 'l': [0, -1], 'r': [0, 1] }
    cant_go = ''
    global lines

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
            if direction[0] in cant_go or direction[-1] in cant_go:
                continue
            curr = lines[y + add_y][x + add_x]
            
            if not curr.isnumeric() and curr != '.':
                return True
    return False

lines = open('input.txt', 'r').readlines()
number = ''
y = 0
x = 0
result = 0

while y < len(lines):
    while x < len(lines[y]):
        if lines[y][x].isnumeric():
            while lines[y][x].isnumeric():
                number += lines[y][x]
                if len(number) == 1:
                    start = x
                x += 1

            end = x
            adj = check(start, end, y)
            if adj:
                result += int(number)
            number = ''
        else:
            x += 1
    y += 1
    x = 0

print(result)
