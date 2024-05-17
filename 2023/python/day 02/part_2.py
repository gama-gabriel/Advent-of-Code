lines = open('input.txt', 'r').readlines()
result = 0
minimum = {'blue': 0, 'green': 0, 'red': 0}

for line in lines:
    line = line.strip()
    game, sets = line.split(':')
    name, index = game.split()
    subsets = sets.replace(';', ',')
    pulls = subsets.split(',')
    pulls = [pull.strip() for pull in pulls]

    for pull in pulls:
        pull = pull.split()
        if int(pull[0]) > minimum[pull[1]]:
            minimum[pull[1]] = int(pull[0])

    power = minimum['blue'] * minimum['green'] * minimum['red']
    result += power
    minimum = {'blue': 0, 'green': 0, 'red': 0}
    

print(result)

