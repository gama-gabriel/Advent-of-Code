lines = open('day_10_input.txt').readlines()
clocks = 0
x = 1
crt = 0
message = ''

def check(clock):
    global message
    if clock in [x, x + 1, x + 2]:
        message += '#'
    else:
        message += '.'
    if clock % 40 == 0:
        clock -= 40
        message+= '\n'
    return clock

for line in lines:
    commands = line.strip().split()
    if commands[0] == 'noop':
        clocks += 1
        crt += 1
        clocks = check(clocks)
    else: 
        for i in range(2):
            clocks += 1
            crt += 1
            clocks = check(clocks)
        x += int(commands[1])    

print(message)
