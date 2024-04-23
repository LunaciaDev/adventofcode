from hashlib import md5

inputFile = open("input")
inputStream = inputFile.read()

DIRECTIONS = ['U', 'D', 'L', 'R']

def taskOne(inputStream):
    stateQueue = [[(0, 0), ""]]

    while True:
        currentState = stateQueue.pop(0)
        currentHash = md5((inputStream + currentState[1]).encode()).hexdigest()[:4]
        
        searchQueue = [
            (currentState[0][0]-1, currentState[0][1]),
            (currentState[0][0]+1, currentState[0][1]),
            (currentState[0][0], currentState[0][1]-1),
            (currentState[0][0], currentState[0][1]+1)
        ]

        for searchIndex in range(len(searchQueue)):
            currentSearchItem = searchQueue[searchIndex]

            if currentSearchItem[0] < 0 or currentSearchItem[0] > 3: continue
            if currentSearchItem[1] < 0 or currentSearchItem[1] > 3: continue

            if ord(currentHash[searchIndex]) <= 97:
                continue

            if currentSearchItem[0] == 3 and currentSearchItem[1] == 3:
                return currentState[1] + DIRECTIONS[searchIndex]
            
            stateQueue.append([currentSearchItem, currentState[1] + DIRECTIONS[searchIndex]])

def taskTwo(inputStream):
    stateQueue = [[(0, 0), ""]]
    maxDist = 0

    while True:
        currentState = stateQueue.pop(0)
        currentHash = md5((inputStream + currentState[1]).encode()).hexdigest()[:4]
        
        searchQueue = [
            (currentState[0][0]-1, currentState[0][1]),
            (currentState[0][0]+1, currentState[0][1]),
            (currentState[0][0], currentState[0][1]-1),
            (currentState[0][0], currentState[0][1]+1)
        ]

        for searchIndex in range(len(searchQueue)):
            currentSearchItem = searchQueue[searchIndex]

            if currentSearchItem[0] < 0 or currentSearchItem[0] > 3: continue
            if currentSearchItem[1] < 0 or currentSearchItem[1] > 3: continue

            if ord(currentHash[searchIndex]) <= 97:
                continue

            if currentSearchItem[0] == 3 and currentSearchItem[1] == 3:
                currentPathLength = len(currentState[1]) + 1
                maxDist = maxDist if currentPathLength <= maxDist else currentPathLength
                continue
            
            stateQueue.append([currentSearchItem, currentState[1] + DIRECTIONS[searchIndex]])

        if len(stateQueue) == 0: return maxDist

print(taskOne(inputStream)) # DUDDRLRRRD
print(taskTwo(inputStream)) # 578
