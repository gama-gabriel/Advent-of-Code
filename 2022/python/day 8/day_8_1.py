with open('day_8_input.txt', 'r') as file:
    lines = file.readlines()
    height = len(lines)
    seen = 0
    inner = 0
    for y, line in enumerate(lines):
        width = len(line.strip())
        for x, letter in enumerate(line.strip()):
            if x > width:
                continue

            if (y == 0) or (y == (height - 1)) or (x == 0) or (x == (width - 1)):
                seen += 1
                continue
            
            letter = int(letter)
                    
            prior_r = [int(item) for index, item in enumerate(line.strip()) if index > x and index <= width]
            right = [int(lines[y][i]) for i in range(x + 1, width)]
            right = max(right)

            prior_l = [int(item) for index, item in enumerate(line) if index < x]            
            left = [int(lines[y][i]) for i in range(x)]
            left = max(left)
            
            prior_u = [int(item[x]) for index, item in enumerate(lines) if index < y]
            up = [int(lines[i][x]) for i in range(y)]
            up = max(up)

            prior_d = [int(item[x]) for index, item in enumerate(lines) if index > y and index <= height]
            down = [int(lines[i][x]) for i in range (y + 1, height)]
            down = max(down) 

            if (letter > up) or (letter > down) or (letter > left) or (letter > right):
                seen += 1
                inner += 1
                
    print(seen)
    print(inner)
            
