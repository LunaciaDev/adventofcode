from hashlib import md5

inputFile = open("input")
inputStream = inputFile.read()

def taskOne(inputStream):
    checkQueue = []
    foundIndices = []
    hashFoundCount = 0
    currentIndex = 0
    stopAddItem = False
    
    while True:
        attemptString = md5((inputStream + str(currentIndex)).lower().encode()).hexdigest()

        indicesToRemove = []

        for index in range(len(checkQueue)):
            check = checkQueue[index]
            
            if attemptString.count(check[0]) != 0:
                indicesToRemove.append(index)
                foundIndices.append(check[1])
                hashFoundCount += 1

                if hashFoundCount == 64:
                    stopAddItem = True
            
            if check[1] + 1000 == currentIndex:
                indicesToRemove.append(index)
        
        for index in reversed(indicesToRemove):
            checkQueue.pop(index)

        for hashIndex in range(len(attemptString)-2):
            if (attemptString[hashIndex] == attemptString[hashIndex+1] and attemptString[hashIndex] == attemptString[hashIndex+2] and not stopAddItem):
                checkQueue.append(["".join([attemptString[hashIndex] for _ in range(5)]), currentIndex])
                break
        
        currentIndex += 1

        if len(checkQueue) == 0 and stopAddItem:
            break

    foundIndices.sort()
    return foundIndices[63]

def taskTwo(inputStream):
    checkQueue = []
    foundIndices = []
    hashFoundCount = 0
    currentIndex = 0
    stopAddItem = False
    
    while True:
        attemptString = inputStream + str(currentIndex)
        
        for _ in range(2017):
            attemptString = md5(attemptString.lower().encode()).hexdigest()

        indicesToRemove = []

        for index in range(len(checkQueue)):
            check = checkQueue[index]
            
            if attemptString.count(check[0]) != 0:
                indicesToRemove.append(index)
                foundIndices.append(check[1])
                hashFoundCount += 1

                if hashFoundCount == 64:
                    stopAddItem = True
            
            if check[1] + 1000 == currentIndex:
                indicesToRemove.append(index)
        
        for index in reversed(indicesToRemove):
            checkQueue.pop(index)

        for hashIndex in range(len(attemptString)-2):
            if (attemptString[hashIndex] == attemptString[hashIndex+1] and attemptString[hashIndex] == attemptString[hashIndex+2] and not stopAddItem):
                checkQueue.append(["".join([attemptString[hashIndex] for _ in range(5)]), currentIndex])
                break
        
        currentIndex += 1

        if len(checkQueue) == 0 and stopAddItem:
            break

    foundIndices.sort()
    return foundIndices[63]

print(taskOne(inputStream))
print(taskTwo(inputStream))
