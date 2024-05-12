lines = open('day_9_input.txt', 'r').readlines()

touch = [-1, 0, 1]
went = set()
rope = []
for _ in range(10):
    rope.append([0, 0])


def move(h_x, h_y, t_x, t_y):
    x_diff = h_x - t_x
    y_diff = h_y - t_y

    # distance = complex((x_diff.real > 0) - (x_diff.real < 0), (y_diff.real > 0) - (y_diff.real < 0))
    # add_x = int(distance.real)
    # add_y = int(distance.imag)
    # t_x += add_x
    # t_y += add_y

    w_x = 0
    w_y = 0

    if (x_diff in [2, -2]):
        w_x = int(x_diff / 2)
        if y_diff in [1, -1]:
            w_y = y_diff

    if (y_diff in [2, -2]):
        w_y = int(y_diff / 2)
        if x_diff in [1, -1]:
            w_x = x_diff

    t_x += w_x
    t_y += w_y
    return[t_x, t_y]

def make_directions(lines):
    directions = []
    for line in lines:
        direction, count = line.strip().split()
        for _ in range(int(count)):
            directions.append(direction.lower())
    return directions

directions = make_directions(lines)

for letter in directions:
    for i, knot in enumerate(rope):
        if i == 9:
            current = f'{knot[0]}, {knot[1]}'
            went.add(current)
        if i == 0:
            if letter == 'u':
                knot[1]  += 1 

            if letter == 'd':
                knot[1] -= 1

            if letter == 'l':
                knot[0] -= 1

            if letter == 'r':
                knot[0] += 1
            continue
        
        else:
            if (rope[i - 1][0] - knot[0] in touch) and (rope[i - 1][1] - knot[1] in touch):
                continue
            x, y = move(rope[i - 1][0], rope[i - 1][1], knot[0], knot[1])
            knot[0] = x
            knot[1] = y

       
current = f'{rope[9][0]}, {rope[9][1]}'

went.add(current)

print(len(went))
