inputFile = open("input")
inputStream = inputFile.read()

#Sanitizing input
inputStream = inputStream.strip().split("\n")
for index in range(len(inputStream)):
    inputStream[index] = int(inputStream[index])

def taskOne(inputStream):
    triangleSideLength = inputStream[0] - 1
    maxSide = ((inputStream[1] + triangleSideLength) * (inputStream[1] + triangleSideLength + 1)) // 2
    iterationCount = maxSide - triangleSideLength

    num = 20151125
    for _ in range(iterationCount-1):
        num = (num * 252533) % 33554393

    print(num)

def taskTwo(inputStream):
    pass

taskOne(inputStream)
taskTwo(inputStream)