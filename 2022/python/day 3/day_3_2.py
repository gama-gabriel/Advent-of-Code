with open("day 3/day_3_input.txt", "r") as file:
    content = file.readlines()
    total = 0
    current = ''
    count = 1
    for i in range(0, len(content)):
        line = content[i]
        if count % 3 == 0:
            prev = content[i - 1]
            prev_prev = content[i - 2]

            for item in line:
                if item in prev and item in prev_prev:
                    current = item
                    break
            
            if current.isupper():
                value = ord(current) - 38
            elif current.islower():
                value = ord(current) - 96
            total += value
        count +=1

print(total)