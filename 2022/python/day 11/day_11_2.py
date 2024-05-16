import math

class Monkey():
    def __init__(self, name, items, operation, test, true, false):
        self.name = name
        self.items = items
        self.operation = operation
        self.test = test
        self.true = true
        self.false = false
        self.inspected = 0

    def inspect(self, monkey_list):
        for item in self.items:
            operation = self.operation.strip().split()
            expression = operation[3:]
           
            expression[0] = item

            if expression[2] == 'old':
                expression[2] = item
            else:
                expression[2] = int(expression[2])
                
            if expression[1] == '+':
                worry = expression[0] + expression[2]

            if expression[1] == '*':
                worry = expression[0] * expression[2]

            global lcd
            worry = worry % lcd
            condition = self.test.strip().split()
            condition = int(condition[3]) 
            
            if worry % condition == 0:
                throw_to = self.true.strip().split()
                throw_to = int(throw_to[5])
                monkey_list[throw_to].items.append(worry) 
            else:
                throw_to = self.false.strip().split()
                throw_to = int(throw_to[5])
                monkey_list[throw_to].items.append(worry) 
            self.inspected += 1
                
        self.items = []

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def calculate_lcm(condition_values):
    result = condition_values[0]
    for value in condition_values[1:]:
        result = lcm(result, value)
    return result

monkey_list = []
lines = open('day_11_input.txt', 'r').readlines()
monkey_business = 0

condition_values = [int(line.split()[-1]) for line in lines if line.startswith("  Test:")]
lcd = calculate_lcm(condition_values)
print("LCD of all conditions:", lcd)

for i in range(0, len(lines), 7):
    name = lines[i].strip(':')
    name = name.strip()

    items = []
    items_raw = lines[i+1].split()
    for item in items_raw[2:]:
        items.append(int(item.strip(','))) 

    operation = lines[i+2].strip()
    test = lines[i+3].strip()
    true = lines[i+4].strip()
    false = lines[i+5].strip()

    monkey = Monkey(name, items, operation, test, true, false)
    monkey_list.append(monkey)
for _ in range(10000):
    for monkey in monkey_list:
        monkey.inspect(monkey_list)

mk = [monkey.inspected for monkey in monkey_list]
mk.sort(reverse = True)
print(mk[0] * mk[1])
print(mk)

