DATA_FILE = r"7\data.txt"

output = []


class File(object):
    def __init__(self, name, size, parentDir) -> None:
        self.size = size
        self.parentDir = parentDir
        self.name = name
    
    def isDir(self):
        return False


class Directory(object):
    def __init__(self, name, parentDir) -> None:
        self.name = name
        self.parentDir = parentDir
        self.childNodes = {}
        self.size = 0

    def updateSize(self, size) -> None:
        self.size += size
        if self.parentDir != None:
            self.parentDir.updateSize(size)

    def addFileChild(self, name, size) -> None:
        fileChild = File(name, size, self)
        if name not in self.childNodes:
            self.childNodes[name] = fileChild
        self.updateSize(size)

    def addDirChild(self, name) -> None:
        childDir = Directory(name, self)
        if name not in self.childNodes:
            self.childNodes[name] = childDir

    def isDir(self):
        return True


def readConsole(textLine):
    if textLine[0] == "$":
        readInstruction(textLine[2:], currentDir)
        #print(outputLine[2:])
    else:
        readOutput(textLine, currentDir, rootDir)


def readInstruction(instruction: str, currentDir: list):
    instructionParts = instruction.split()
    if instructionParts[0] == "cd":
        if instructionParts[1] == "/":
            currentDir = ["/"]
        elif instructionParts[1] == "..":
            currentDir.pop()
        else:
            currentDir.append(instructionParts[1] + "/")

def readOutput(output: str, dirTrail: list, rootDir: Directory):
    outputParts = output.split()
    if outputParts[0] == "dir":
        currentDir = rootDir
        for dir in dirTrail[1:]:
            currentDir = currentDir.childNodes[dir]
        currentDir.addDirChild(outputParts[1]+"/")
    else:
        currentDir = rootDir
        for dir in dirTrail[1:]:
            currentDir = currentDir.childNodes[dir]
        currentDir.addFileChild(outputParts[1], int(outputParts[0]))
        
def calculateSpaceRecur(directory: Directory, spaceToFree: int, sizes: list):
    
    if directory.size >= spaceToFree:
        sizes.append((directory.size))
    
    for child in directory.childNodes:
        node = directory.childNodes[child]
        if node.isDir():
            calculateSpaceRecur(node, spaceToFree, sizes)
    
    pass

def step1(directory: Directory):
    sizeSum = 0
    if directory.size <= 100000:
        sizeSum += directory.size
    
    for child in directory.childNodes:
        node = directory.childNodes[child]
        if node.isDir():
            sizeSum += step1(node)
    
    return sizeSum

def step2(directory: Directory):
    freeSpace = 70000000 - directory.size
    spaceToFree = 30000000 - freeSpace

    sizes = []
    calculateSpaceRecur(directory, spaceToFree, sizes)
    return sizes

with open(DATA_FILE, "r") as f:
    output = f.read().splitlines()

currentDir = ["/"]
rootDir = Directory("/", None)

for line in output:
    readConsole(line)


sizes = step2(rootDir)
print(min(sizes))