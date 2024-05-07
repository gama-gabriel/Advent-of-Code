with open("day 3/day_3_input.txt", "r") as file:
    content = file.readlines()
    total = 0
    current = ''
    for line in content:
        length = len(line)
        half = length / 2
        value = 0
        first_half = line[:int(half)]
        sec_half = line[int(half):]

        for item in first_half:
            if item in sec_half:
                current = item
                break
        
        if current.isupper():
            value = ord(current) - 38
        elif current.islower():
            value = ord(current) - 96
        total += value

print(total)