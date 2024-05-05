with open("day_1_input.txt", 'r') as file:
    content = file.readlines()
    current = 0
    cal_list = []
    for line in content:
        if line == '\n':
            cal_list.append(current)
            current = 0
            continue
        current += int(line.split("\n")[0])

cal_list.sort(reverse=True)
print(cal_list[0] + cal_list[1] + cal_list[2])