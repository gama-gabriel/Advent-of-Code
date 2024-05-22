lines = open('input.txt', 'r').readlines()
lines = [line.split(':') for line in lines]
lines = [line[1].strip() for line in lines]
result = 0

for line in lines:
    winners, mine = line.split('|')
    winners = [int(item) for item in winners.split()]
    mine = [int(item) for item in mine.split()]
    count = 0

    for number in mine:
        if number in winners:
            count += 1

    if count ==  0:
        continue

    result += 2**(count - 1)

print(result)
    
