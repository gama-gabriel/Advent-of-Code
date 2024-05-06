with open("day 2/day_2_input.txt", "r") as file:
    content = file.readlines()
    score = 0
    keys = {"rock": {"beats": "scissors", "draws": 'rock', "loses": "paper"}, "paper": {"beats": "rock", "draws": 'paper', "loses": "scissors"}, "scissors": {"beats": "paper", "draws": 'scissors', "loses": "rock"}}
    for line in content:
        opp = ""
        me = ""
        plays = line.split()
        if plays[0].lower() == 'a':
            opp = "rock"
        elif plays[0].lower() == 'b':
            opp = "paper"
        elif plays[0].lower() == 'c':
            opp = "scissors"
        
        if plays[1].lower() == 'x':
            me = keys[opp]["beats"]
        elif plays[1].lower() == 'y':
            me = keys[opp]["draws"]
            score += 3
        elif plays[1].lower() == 'z':
            me = keys[opp]["loses"]
            score += 6
        
        if me == "rock":
            score += 1
        elif me == "paper":
            score += 2
        elif me == "scissors":
            score += 3

print(score)
    


