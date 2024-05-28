lines = open('input.txt', 'r').readlines()
lines = [line.split(':') for line in lines]
lines = [[line[0].split()[1], line[1].strip()] for line in lines]
result = 0
cards = {}

for line in lines:
    cards[line[0]] = 1


for line in lines:
    card, numbers = line

    winners, mine = numbers.split('|')
    winners = [int(item) for item in winners.split()]
    mine = [int(item) for item in mine.split()]
    count = 0
    possess = cards[card]

    for number in mine:
        if number in winners:
            count += 1

    for i in range(1, count + 1):
        cards[f'{int(card) + i}'] += possess



for total in cards.values():
    result += total

print(result)
    
end = perf_counter()
