with open("day 2/day_2_input.txt", "r") as file:
    content = file.readlines()
    score = 0
    keys = {"rock": ['a', 'x'], "paper": ['b', 'y'], "scissors": ['c', 'z']}
    for line in content:
        opp = ""
        me = ""
        plays = line.split()
        if plays[0].lower() in keys['rock']:
            opp = "rock"
        if plays[0].lower() in keys['paper']:
            opp = "paper"
        if plays[0].lower() in keys['scissors']:
            opp = "scissors"
        
        if plays[1].lower() in keys['rock']:
            me = "rock"
            score += 1
        if plays[1].lower() in keys['paper']:
            me = "paper"
            score += 2
        if plays[1].lower() in keys['scissors']:
            me = "scissors"
            score += 3
        
        if opp == me:
            score += 3
            continue
        if (opp == 'scissors' and me == 'rock') or (opp == 'rock' and me == 'paper') or (opp == 'paper' and me == 'scissors'):
            score += 6

print(score)
    


