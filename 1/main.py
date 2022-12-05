lines = []

with open(".\data.txt", "r") as f:
    data = f.read()
    lines = data.split("\n")

amounts = []
tmp = 0
for line in lines:
    if line != "":
        tmp += int(line)
    else:
        amounts.append(tmp)
        tmp = 0

amounts.sort(reverse=True)

print(amounts[0]+amounts[1] + amounts[2])