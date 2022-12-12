INSTRUCTION_PATTERN = r'move (\d+) from (\d) to (\d)'
DATA_FILE = r"5\\data.txt"

import re

stacks = []

with open(DATA_FILE, "r") as f:
    for line in f:
        numbers = re.findall(r'\d+', line)
        if numbers != []:
            for i in range(int(numbers[-1])):
                stacks.append([])
            break
    
with open(DATA_FILE, "r") as f:
    for line in f:
        if line.startswith(" 1"):
            break
        for i in range(len(stacks)):
            crate = line[4*i:4*i+4]
            char = re.search(r'\[([A-Z])\]', crate)
            if char:
                stacks[i].append(char.group(1))
    for i in stacks:
        i.reverse()

with open(DATA_FILE, "r") as f:
    for line in f:
        instruction = re.match(INSTRUCTION_PATTERN, line)
        if instruction:
            tmp = []
            for i in range(int(instruction.group(1))):
                tmp.append(stacks[int(instruction.group(2))-1].pop())
            tmp.reverse()
            stacks[int(instruction.group(3))-1] = stacks[int(instruction.group(3))-1] + tmp
solution = ""
for i in stacks:
    solution += i[-1]
print(solution)