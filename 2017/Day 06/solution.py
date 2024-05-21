from copy import deepcopy

inputFile = open("input")
inputStream = inputFile.read().strip().split('\t')

for index in range(len(inputStream)):
    inputStream[index] = int(inputStream[index])

loopSize = 0

def taskOne(inputStream):
    global loopSize
    memoryBanks = deepcopy(inputStream)
    memoryBankCount = len(memoryBanks)
    encounteredSet = []
    cycleCount = 0

    while True:
        foundSet = True

        try:
            encounteredSet.index(memoryBanks)
        except:
            foundSet = False
            encounteredSet.append(deepcopy(memoryBanks))
        
        if foundSet:
            loopSize = cycleCount - encounteredSet.index(memoryBanks)
            break
        
        boxCount = memoryBanks[0]
        maxIndex = 0

        for index in range(len(memoryBanks)):
            if memoryBanks[index] > boxCount:
                maxIndex = index
                boxCount = memoryBanks[index]

        memoryBanks[maxIndex] = 0
        index = (maxIndex+1) % memoryBankCount

        while boxCount > 0:
            memoryBanks[index] += 1
            boxCount -= 1
            index = (index + 1) % memoryBankCount
        
        cycleCount += 1
    
    print(cycleCount)

def taskTwo(inputStream):
    print(loopSize)

taskOne(inputStream)
taskTwo(inputStream)