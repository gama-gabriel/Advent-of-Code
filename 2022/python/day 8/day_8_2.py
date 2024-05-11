with open('day_8_input.txt', 'r') as file:
    lines = file.readlines()
    height = len(lines)
    high_score = 0

    for y, line in enumerate(lines):
        width = len(line.strip())
        for x, letter in enumerate(line.strip()):
            if (y == 0) or (y == (height - 1)) or (x == 0) or (x == (width - 1)):
                continue
            
            letter = int(letter)
                    
            right = []
            for i in range(x + 1, width):
                right.append(int(lines[y][i])) 
                if int(lines[y][i]) >= letter:
                    break

            left = []
            for i in range(x - 1, -1, -1):
                left.append(int(lines[y][i])) 
                if int(lines[y][i]) >= letter:
                    break
            
            up = []
            for i in range(y -1, -1, -1):
                up.append(int(lines[i][x])) 
                if int(lines[i][x]) >= letter:
                    break

            down = []
            for i in range(y + 1, height):
                down.append(int(lines[i][x])) 
                if int(lines[i][x]) >= letter:
                    break

            score = len(right) * len(left) * len(up) * len(down)  
            if score > high_score:
                high_score = score

    print(high_score)
            
