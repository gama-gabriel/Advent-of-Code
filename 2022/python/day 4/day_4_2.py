with open("day 4/day_4_input.txt", "r") as file:
    content = file.readlines()
    count = 0

    for line in content:
        pair = line.split(",")
        first = pair[0].split("-")
        second = pair[1].split("-")
        # this one was tuff
        if (int(first[1]) >= int(second[0]) and int(first[0]) <= int(second[1])) or (int(second[1]) >= int(first[0]) and int(second[0]) <= int(first[1])):
            count += 1
    
print(count)