lines = open('input.txt', 'r').readlines()
limits = {'red': 12, 'green': 13, 'blue': 14}
result = 0

for line in lines:
    line = line.strip()
    game, sets = line.split(':')
    name, index = game.split()
    subsets = sets.replace(';', ',')
    pulls = subsets.split(',')
    pulls = [pull.strip() for pull in pulls]

    for pull in pulls:
        pull = pull.split()
        if int(pull[0]) > limits[pull[1]]:
            possible = False
            break
        possible = True

    if possible:
        result += int(index)

print(result)

