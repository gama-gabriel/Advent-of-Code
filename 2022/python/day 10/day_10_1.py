lines = open('day_10_input.txt').readlines()
clocks = 0
x = 1
ss = []

def check(clock):
    if (clock + 20) % 40 == 0 and len(ss) <= 6:
        ss.append(clock * x)

for line in lines:
    commands = line.strip().split()
    if commands[0] == 'noop':
        clocks += 1
        check(clocks)
    else: 
        for i in range(2):
            clocks += 1
            check(clocks)
        x += int(commands[1])    
print(sum(ss))
print(ss)
