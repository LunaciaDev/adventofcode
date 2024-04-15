inputFile = open("input")
inputStream = inputFile.read()

def taskOne(inputStream):
    currentFloor = 0

    for character in inputStream:
        if character == "(":
            currentFloor += 1
            continue
        currentFloor -= 1
    
    print(currentFloor) #138

def taskTwo(inputStream):
    currentFloor = 0
    position = 0

    for character in inputStream:
        position += 1
        if character == "(":
            currentFloor += 1
            continue
        
        #Since Santa is going down a floor, we know that
        #he is going to the basement if his current floor is 0
        if currentFloor == 0:
            break

        currentFloor -= 1

    print(position) #1771

taskOne(inputStream)
taskTwo(inputStream)