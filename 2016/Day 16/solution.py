from copy import copy

inputFile = open("input")
inputStream = inputFile.read()

def taskOne(inputStream):
    targetLength = 272
    currentFill = copy(inputStream)

    while len(currentFill) < targetLength:
        newFill = list(reversed(currentFill))
        
        for charIndex in range(len(newFill)):
            if newFill[charIndex] == '0':
                newFill[charIndex] = '1'
            else:
                newFill[charIndex] = '0'
        
        newFill = "".join(newFill)
        currentFill += '0' + newFill
    
    currentFill = currentFill[:targetLength]
    currentChecksum = copy(currentFill)

    while len(currentChecksum) % 2 == 0:
        newChecksum = ""

        for charIndex in range(0, len(currentChecksum), 2):
            if currentChecksum[charIndex] == currentChecksum[charIndex+1]:
                newChecksum += '1'
            else:
                newChecksum += '0'
        
        currentChecksum = newChecksum

    return currentChecksum

def taskTwo(inputStream):
    targetLength = 35651584
    currentFill = copy(inputStream)

    while len(currentFill) < targetLength:
        newFill = list(reversed(currentFill))
        
        for charIndex in range(len(newFill)):
            if newFill[charIndex] == '0':
                newFill[charIndex] = '1'
            else:
                newFill[charIndex] = '0'
        
        newFill = "".join(newFill)
        currentFill += '0' + newFill
    
    currentFill = currentFill[:targetLength]
    currentChecksum = copy(currentFill)

    while len(currentChecksum) % 2 == 0:
        newChecksum = ""

        for charIndex in range(0, len(currentChecksum), 2):
            if currentChecksum[charIndex] == currentChecksum[charIndex+1]:
                newChecksum += '1'
            else:
                newChecksum += '0'
        
        currentChecksum = newChecksum

    return currentChecksum

print(taskOne(inputStream))
print(taskTwo(inputStream))