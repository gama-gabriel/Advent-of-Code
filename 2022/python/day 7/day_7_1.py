class Dir:
    def __init__(self, name):
        self.name = name
        self.size = 0
        self.children = []
        self.parent = None 
        
    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def get_size(self) -> int:
        curr_size = 0
        for child in self.children:
            curr_size += child.get_size()
        return curr_size

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.parent = None
        
    def get_size(self):
        return self.size

def cd(path, current):
    if path[2] == '..':
        return current.parent
        
    for item in current.children:
        if item.name == path[2]:
            return item

def traverse(tree, sum):
    if isinstance(tree, Dir):
        if (tree.get_size() <= 100000):
            print(tree.name)
            print(tree.get_size())
            sum.append(tree.get_size())
        for child in tree.children:
            traverse(child, sum)
    return sum

with open('day 7/day_7_input.txt', 'r') as file:
    lines = file.readlines()
    current = Dir('/')
    lista = []
    soma = 0
    for i, line in enumerate(lines):
        words = line.split()

        if words[0] != '$':
            continue

        if words[1] == 'cd':
            if words[2] == '/':
                continue
            current = cd(words, current)
            continue

        if words[1] == 'ls':
            i +=1 
            while lines[i].split()[0] != '$':
                words = lines[i].split()
                if words[0] == 'dir':
                    dir = Dir(words[1])
                    current.add_child(dir)
                else:
                    file = File(words[1], int(words[0]))
                    current.add_child(file)
                i += 1
                if i == len(lines):
                    break

        lista.append(current)

    while current.name != '/':
        current = current.parent
    l = traverse(current, [])
    print(sum(l))
