duels = []
score = 0

with open("data.txt", "r") as f:
    data = f.read()
    lines = data.split("\n")
    for line in lines:
        duels.append(tuple(line.split()))

'''
for duel in duels:
    match duel[1]:
        case 'X':
            score += 1
            if duel[0] == 'A':
                score += 3
            elif duel[0] == 'B':
                score += 0
            else:
                score += 6
        case 'Y':
            score += 2
            if duel[0] == 'A':
                score += 6
            elif duel[0] == 'B':
                score += 3
            else:
                score += 0
        case _ :
            score += 3
            if duel[0] == 'A':
                score += 0
            elif duel[0] == 'B':
                score += 6
            else:
                score += 3
'''

for duel in duels:
    match duel[1]:
        case 'X':
            score += 0
            if duel[0] == 'A':
                score += 3
            elif duel[0] == 'B':
                score += 1
            else:
                score += 2
        case 'Y':
            score += 3
            if duel[0] == 'A':
                score += 1
            elif duel[0] == 'B':
                score += 2
            else:
                score += 3
        case _ :
            score += 6
            if duel[0] == 'A':
                score += 2
            elif duel[0] == 'B':
                score += 3
            else:
                score += 1    

print(score)