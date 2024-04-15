inputFile = open("input")
inputStream = inputFile.read()

def taskOne(inputStream):
    currentIndex = 0
    inputLength = len(inputStream) - 1
    extractedStreamLength = 0

    while currentIndex <= inputLength:
        if inputStream[currentIndex] == "(":
            bracketStart = currentIndex

            while currentIndex <= inputLength:
                currentIndex += 1
                if inputStream[currentIndex] == ")": break
            
            bracketEnd = currentIndex
            expansionData = inputStream[bracketStart+1 : bracketEnd].split("x")
            
            currentIndex += int(expansionData[0]) + 1

            extractedStreamLength += int(expansionData[0]) * int(expansionData[1])

            continue

        startingIndex = currentIndex

        while currentIndex < inputLength:
            if inputStream[currentIndex+1] == "(": break
            currentIndex += 1
        
        extractedStreamLength += currentIndex - startingIndex + 1
        
        currentIndex += 1
    
    print(extractedStreamLength) # 110346

def taskTwo(inputStream):
    currentIndex = 0
    inputLength = len(inputStream) - 1
    extractedStreamLength = 0

    while currentIndex <= inputLength:
        if inputStream[currentIndex] == "(":
            bracketStart = currentIndex

            while currentIndex <= inputLength:
                currentIndex += 1
                if inputStream[currentIndex] == ")": break
            
            bracketEnd = currentIndex
            expansionData = inputStream[bracketStart+1 : bracketEnd].split("x")
            
            currentIndex += int(expansionData[0]) + 1

            extractedStreamLength += taskTwo(inputStream[bracketEnd + 1 : bracketEnd + 1 + int(expansionData[0])]) * int(expansionData[1])

            continue

        startingIndex = currentIndex

        while currentIndex < inputLength:
            if inputStream[currentIndex+1] == "(": break
            currentIndex += 1
        
        extractedStreamLength += currentIndex - startingIndex + 1
        
        currentIndex += 1
    
    return(extractedStreamLength)

taskOne(inputStream)
print(taskTwo(inputStream)) #10774309173
