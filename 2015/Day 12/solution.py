inputFile = open("input")
inputStream = inputFile.read()

def taskOne(inputStream):
    jsonSize = len(inputStream)
    index = 0
    total = 0
    
    while index < jsonSize:
        if inputStream[index].isnumeric() or inputStream[index] == "-":
            startNumIndex = index
            index += 1

            while inputStream[index].isnumeric():
                index += 1

            total += int(inputStream[startNumIndex:index])
            continue
        
        index += 1

    print(total)

def taskTwo(inputStream):
    '''
    For Task Two, we simply remove any object that have property "red"
    and ignore "red" that is in an array. Sounds simple enough.
    We keep track of the opening bracket, opening array and any red we have found so far.
    When we close an object, we check if any "red" is in object and delete/ignore based on that.
    Same goes for array, but we just stop tracking that red instead of removing the array.
    Is it faster than converting JSON to dict? Maybe.
    Is it a bigger headache? Yes!
    '''
    jsonSize = len(inputStream)
    objectLevel = []
    arrayLevel = []
    redLevel = []
    index = 0

    while index < jsonSize:
        if inputStream[index] == "{":
            objectLevel.append(index)
            index += 1
            continue

        if inputStream[index] == "[":
            arrayLevel.append(index)
            index += 1
            continue

        if inputStream[index:index+3] == "red":
            redLevel.append(index)
            index += 2
            continue

        if inputStream[index] == "]":
            if len(redLevel) != 0:
                redIndex = 0
                redRange = len(redLevel)
                while redIndex < redRange:
                    if redLevel[redIndex] > arrayLevel[-1]:
                        redLevel.pop(redIndex)
                        redRange -= 1
                        continue

                    redIndex += 1

            arrayLevel.pop()
            index += 1
            continue

        if inputStream[index] == "}":
            if len(redLevel) == 0:
                objectLevel.pop()
                index += 1
                continue
            
            if redLevel[-1] < objectLevel[-1]:
                objectLevel.pop()
                index += 1
                continue

            startIndex = objectLevel.pop()
            redIndex = 0
            redRange = len(redLevel)
            while redIndex < redRange:
                if redLevel[redIndex] > startIndex:
                    redLevel.pop(redIndex)
                    redRange -= 1
                    continue

                redIndex += 1

            inputStream = inputStream[:startIndex] + inputStream[index+1:]
            jsonSize = jsonSize - (index - startIndex) - 1
            index = startIndex
            continue

        index += 1

    index = 0
    jsonSize = len(inputStream)
    total = 0
    
    while index < jsonSize:
        if inputStream[index].isnumeric() or inputStream[index] == "-":
            startNumIndex = index
            index += 1

            while inputStream[index].isnumeric():
                index += 1

            total += int(inputStream[startNumIndex:index])
            continue
        
        index += 1    

    print(total)

taskOne(inputStream)
taskTwo(inputStream)