inputFile = open("input")
inputStream = inputFile.read()

#Convert inputStream to array and converting string to number to make it easier to work with
inputStream = inputStream.split("\n")
for index in range(len(inputStream)):
    inputStream[index] = inputStream[index].split("x")
    for index2 in range(3):
        inputStream[index][index2] = int(inputStream[index][index2])
    #Sort the length sizes to streamline both task
    inputStream[index].sort()

def taskOne(inputStream):
    wrappingPaperSize = 0
    
    for present in inputStream:
        wrappingPaperSize += 3*present[0]*present[1] + 2*present[1]*present[2] + 2*present[2]*present[0]
    

    print(wrappingPaperSize)

def taskTwo(inputStream):
    ribbonLength = 0
    
    for present in inputStream:
        ribbonLength += 2*present[0] + 2*present[1] + present[0]*present[1]*present[2]

    print(ribbonLength)

taskOne(inputStream)
taskTwo(inputStream)
