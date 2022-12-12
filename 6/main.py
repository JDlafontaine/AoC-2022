DATA_FILE = r"6\data.txt"

f = open(DATA_FILE, "r")

stream = []

stream = list(f.read(14))

distChar = 14

while True:
    char = f.read(1)
    streamSet = set(stream.copy())
    if len(streamSet) == 14 or char == "":
        break
    else: 
        del stream[0]
        stream.append(char)
        distChar +=1


f.close()
print(distChar)