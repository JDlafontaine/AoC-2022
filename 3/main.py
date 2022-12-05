priority = 0
groups = []
with open("data.txt", "r") as f:
    lines = f.read().splitlines()
    while len(lines) > 0:
        groups.append([set(lines.pop(0)),set(lines.pop(0)),set(lines.pop(0))])

for group in groups:
    tmp = group[0].intersection(group[1], group[2]).pop()
    if tmp.isupper():
        priority += ord(tmp) - ord('A') + 27
    else:
        priority += ord(tmp) - ord('a') + 1

print(priority)
