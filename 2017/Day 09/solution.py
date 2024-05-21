inputFile = open("input")
inputStream = inputFile.read()

def taskOne(inputStream):
    score = 0
    depth = 0
    inTrash = False
    ignoreChar = False

    for character in inputStream:
        if ignoreChar:
            ignoreChar = False
            continue

        match character:
            case '{':
                if not inTrash:
                    depth += 1
            case '}':
                if not inTrash:
                    score += depth
                    depth -= 1
            case '<':
                inTrash = True
            case '>':
                inTrash = False
            case '!':
                ignoreChar = True

    print(score)

def taskTwo(inputStream):
    garbageCount = 0
    inTrash = False
    ignoreChar = False

    for character in inputStream:
        if ignoreChar:
            ignoreChar = False
            continue

        match character:
            case '<':
                if inTrash:
                    garbageCount += 1
                    continue

                inTrash = True
            case '>':
                inTrash = False
            case '!':
                ignoreChar = True
            case _:
                if inTrash:
                    garbageCount += 1

    print(garbageCount)

taskOne(inputStream)
taskTwo(inputStream)