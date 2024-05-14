inputFile = open("input")
inputStream = inputFile.read()

#Sanitizing input
inputStream = inputStream.split("\n")

def taskOne(inputStream):
    errorCorrectedOutput = []
    encodedCharStream = [[0 for _ in range(26)] for _ in range(len(inputStream[0]))]

    for message in inputStream:
        for charIndex in range(len(message)):
            encodedCharStream[charIndex][ord(message[charIndex]) - 97] += 1

    for encodedStream in encodedCharStream:
        maxValFound = -1
        maxValChar = -1
        for valueIndex in range(len(encodedStream)):
            if encodedStream[valueIndex] > maxValFound:
                maxValFound = encodedStream[valueIndex]
                maxValChar = valueIndex + 97

        errorCorrectedOutput.append(chr(maxValChar))
    
    print("".join(errorCorrectedOutput))

def taskTwo(inputStream):
    errorCorrectedOutput = []
    encodedCharStream = [[0 for _ in range(26)] for _ in range(len(inputStream[0]))]

    for message in inputStream:
        for charIndex in range(len(message)):
            encodedCharStream[charIndex][ord(message[charIndex]) - 97] += 1

    for encodedStream in encodedCharStream:
        maxValFound = 800
        maxValChar = -1
        for valueIndex in range(len(encodedStream)):
            if encodedStream[valueIndex] < maxValFound:
                maxValFound = encodedStream[valueIndex]
                maxValChar = valueIndex + 97

        errorCorrectedOutput.append(chr(maxValChar))
    
    print("".join(errorCorrectedOutput))

taskOne(inputStream)
taskTwo(inputStream)
