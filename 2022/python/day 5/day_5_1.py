class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        self.items.pop(0)
    
    def top(self):
        if not self.items:
            return ""
        return self.items[0]
    
    def see(self):
        return self.items
    
def fill_stack(stack: list):
    with open("day 5/day_5_input.txt", "r") as file:
        content = file.readlines()
        items_count = 0
        for i in range(0, 9):
            stack.append(Stack())

        for i in range(7, -1, -1):
            current = content[i]
            stack_count = 0
            for count, letter in enumerate(current):
                if (count + 1) % 4 == 0:
                    stack_count += 1
    
                if (count - 1) % 4 == 0:
                    
                  if letter != " ":
                      items_count += 1
                      stack[stack_count].push(item=letter)
    return stack

stack_list = fill_stack([])
stacks = dict()

for number, item in enumerate(stack_list):
    stacks[number + 1] = item
def go_through():
    with open("day 5/day_5_input.txt", "r") as file:
        content = file.readlines()
        for count, line in enumerate(content):
            if count <= 9:
                continue
            else:
                words = line.split()
                print(words)
                move(int(words[1]), stacks[int(words[3])], stacks[int(words[5])])

def move(quantity, from_stack, to_stack):    
    for i in range(0, quantity):
        to_stack.push(from_stack.top())
        from_stack.pop()

go_through()
string = ""
for i in stacks.values():
    string += i.top()

print(string)    