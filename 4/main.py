
def createRange(rangeStr: str) -> set:
    [start, stop] = rangeStr.split('-')
    return set(range(int(start), int(stop) +1))

with open("4\\data.txt") as f:
    lines = f.read().splitlines()

duplicate = 0

for line in lines:
    first, second = line.split(',') 
    firstRange, secondRange = createRange(first), createRange(second)
    # if (firstRange.issubset(secondRange) or secondRange.issubset(firstRange)):
    if not firstRange.isdisjoint(secondRange):
        duplicate += 1

print(duplicate)
    