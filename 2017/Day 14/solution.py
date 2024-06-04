from math import floor
from collections import deque

inputFile = open("input")
inputStream = inputFile.read().strip()

ROPE_SIZE = 256
DIRECTION = [
    [1, 0],
    [0, 1],
    [-1, 0],
    [0, -1],
]

# Recycling Knot Hash Function
# I feel like this could be optimized...
def knotHash(key):
    lengthArray = [ord(char) for char in key] + [17, 31, 73, 47, 23]

    rope = list(range(ROPE_SIZE))
    skipSize = 0
    currPos = 0

    for _ in range(64):
        for length in lengthArray:
            stepCount = floor(length / 2)
            
            # Doing reversal
            startPtr = currPos
            endPtr = (currPos + length) % ROPE_SIZE
            endPtr = ROPE_SIZE-1 if endPtr == 0 else endPtr - 1

            for _ in range(stepCount):
                temp = rope[startPtr]
                rope[startPtr] = rope[endPtr]
                rope[endPtr] = temp

                startPtr = (startPtr + 1) % ROPE_SIZE
                endPtr = ROPE_SIZE-1 if endPtr == 0 else endPtr - 1
            
            currPos = (currPos + skipSize + length) % ROPE_SIZE
            skipSize += 1

    denseHash = []
    
    for offset in range(16):
        result = rope[16 * offset]
        for target in range(1, 16):
            result ^= rope[16 * offset + target]
        denseHash.append(hex(result)[2:].zfill(2))

    return "".join(denseHash)

def prettyPrinter(grid):
    res = ''
    for row in grid:
        res += "".join(row) + "\n"
    print(res)

def taskOne(inputStream):
    usedBlock = 0
    
    for i in range(128):
        hash = knotHash(inputStream + "-" + str(i))
        binRepresentation = bin(int(hash, 16))[2:].zfill(128)
        
        for bit in binRepresentation:
            if bit == '1': usedBlock += 1
    
    print(usedBlock)

def taskTwo(inputStream):
    grid = []
    regionCount = 0
    
    for i in range(128):
        hash = knotHash(inputStream + "-" + str(i))
        binRepresentation = bin(int(hash, 16))[2:].zfill(128)
        
        grid.append(list(binRepresentation))

    nodeQueue = deque()

    for y in range(128):
        for x in range(128):
            if grid[y][x] == '0': continue

            regionCount += 1
            nodeQueue.append([y, x])
            grid[y][x] = '0'

            while len(nodeQueue) > 0:
                target = nodeQueue.popleft()

                for direction in DIRECTION:
                    newNode = [target[0] + direction[0], target[1] + direction[1]]
                    if min(newNode) < 0 or max(newNode) > 127: continue

                    if grid[newNode[0]][newNode[1]] == '0': continue

                    grid[newNode[0]][newNode[1]] = '0'
                    nodeQueue.append([newNode[0], newNode[1]])
    
    print(regionCount)

taskOne(inputStream)
taskTwo(inputStream)