lines = open('day_9_input.txt', 'r').readlines()

h_x, h_y = [0, 0]
t_x, t_y = [0, 0]
touch = [-1, 0, 1]
went = []

def move(h_x, h_y, t_x, t_y):
    x_diff = h_x - t_x
    y_diff = h_y - t_y
    
    if x_diff == 0:
        t_y += int(y_diff / 2)
        return [t_x, t_y]

    if y_diff == 0:
        t_x += int(x_diff / 2)
        return [t_x, t_y]

    if x_diff in [2, -2]:
        t_x += int(x_diff / 2)
        t_y += y_diff
        return [t_x, t_y]

    t_x += x_diff
    t_y += int(y_diff / 2)
    return [t_x, t_y]

def make_directions(lines):
    directions = []
    for line in lines:
        direction, count = line.strip().split()
        for _ in range(int(count)):
            directions.append(direction.lower())
    return directions

directions = make_directions(lines)

for letter in directions:
    current = f'{h_x}, {h_y}'
    if not(current in went):
        went.append(current)

    if letter == 'u':
        h_y += 1 

    if letter == 'd':
        h_y -= 1

    if letter == 'l':
        h_x -= 1

    if letter == 'r':
        h_x += 1

    if (h_x - t_x in touch) and (h_y - t_y in touch):
        continue
    
    t_x, t_y = move(h_x, h_y, t_x, t_y)


current = f'{h_x}, {h_y}'
print(current)

if not(current in went):
    went.append(current)

print(len(went))
