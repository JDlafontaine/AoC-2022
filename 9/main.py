DATA_FILE = r"9\data.txt"

instructions = []
with open(DATA_FILE, "r") as f:
    for line in f:
        instructions.append(tuple(line.split()))

def step1(instructions):
    headpos = [0, 0]
    tailpos = [0, 0]

    distPosTail = set()

    for instruction in instructions:
        for _ in range(int(instruction[1])):
            if instruction[0] == 'U':            
                headpos[1] += 1
            if instruction[0] == 'D':
                headpos[1] -= 1
            if instruction[0] == 'R':
                headpos[0] += 1
            if instruction[0] == 'L':
                headpos[0] -= 1
            tailpos = updatePos(headpos, tailpos)
            distPosTail.add(tuple(tailpos))
    return len(distPosTail)

def step2(instructions, knotsNr):
    knots = []
    for i in range(knotsNr):
        knots.append([0,0])
    
    distPosTail = set()
    for instruction in instructions:
        for _ in range(int(instruction[1])):
            if instruction[0] == 'U':            
                knots[0][1] += 1
            if instruction[0] == 'D':
                knots[0][1] -= 1
            if instruction[0] == 'R':
                knots[0][0] += 1
            if instruction[0] == 'L':
                knots[0][0] -= 1
            for k in range(1,len(knots)): 
                knots[k] = updatePos(knots[k-1], knots[k])
            distPosTail.add(tuple(knots[-1]))
    return len(distPosTail)

def step3(instructions):
    knotsNr = 1
    distPos = 1
    while True:
        distPos = step2(instructions, knotsNr)
        if distPos != 1:
            #print("{}: {}".format(knotsNr, distPos))
            knotsNr +=1
        else:
            break
    return(knotsNr)

def updatePos(headpos, tailpos):
    if (abs(tailpos[0] - headpos[0]) == 2) or (abs(tailpos[1] - headpos[1]) == 2):
        if tailpos[0] == headpos[0]:
            if tailpos[1] < headpos[1]:
                tailpos[1] += 1
            else:
                tailpos[1] -= 1
        elif tailpos [1] == headpos[1]:
            if tailpos[0] < headpos[0]:
                tailpos[0] += 1
            else:
                tailpos[0] -= 1
        else:
            if tailpos[0] > headpos[0]:
                tailpos[0] -=1
            elif tailpos[0] < headpos[0]:
                tailpos[0] += 1
            if tailpos[1] > headpos[1]:
                tailpos[1] -=1
            elif tailpos[1] < headpos[1]:
                tailpos[1] += 1
    return tailpos

#print(step1(instructions))
#step2Sol = step2(instructions, 10)
#print(step2Sol)
print(step3(instructions))