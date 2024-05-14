inputFile = open("input")
inputStream = inputFile.read()

def taskOne(inputStream):
    colCount = len(inputStream)
    rowCount = 40

    roomTiles = [[0]]

    for tile in inputStream:
        if tile == '^':
            roomTiles[0].append(1)
        else:
            roomTiles[0].append(0)

    roomTiles[0].append(0)

    for index in range(1, rowCount):
        roomTiles.append([0])

        currentRow = roomTiles[index]
        previousRow = roomTiles[index - 1]

        for colIndex in range(1, colCount+1):
            if previousRow[colIndex - 1] == 1 and previousRow[colIndex] == 1 and previousRow[colIndex + 1] == 0:
                currentRow.append(1)
                continue

            if previousRow[colIndex - 1] == 0 and previousRow[colIndex] == 1 and previousRow[colIndex + 1] == 1:
                currentRow.append(1)
                continue

            if previousRow[colIndex - 1] == 1 and previousRow[colIndex] == 0 and previousRow[colIndex + 1] == 0:
                currentRow.append(1)
                continue

            if previousRow[colIndex - 1] == 0 and previousRow[colIndex] == 0 and previousRow[colIndex + 1] == 1:
                currentRow.append(1)
                continue

            currentRow.append(0)

        currentRow.append(0)
    
    trapCount = 0

    for row in roomTiles:
        trapCount += sum(row)
    
    return (colCount * rowCount) - trapCount

def taskTwo(inputStream):
    colCount = len(inputStream)
    rowCount = 400000

    roomTiles = [[0]]

    for tile in inputStream:
        if tile == '^':
            roomTiles[0].append(1)
        else:
            roomTiles[0].append(0)

    roomTiles[0].append(0)

    for index in range(1, rowCount):
        roomTiles.append([0])

        currentRow = roomTiles[index]
        previousRow = roomTiles[index - 1]

        for colIndex in range(1, colCount+1):
            if previousRow[colIndex - 1] == 1 and previousRow[colIndex] == 1 and previousRow[colIndex + 1] == 0:
                currentRow.append(1)
                continue

            if previousRow[colIndex - 1] == 0 and previousRow[colIndex] == 1 and previousRow[colIndex + 1] == 1:
                currentRow.append(1)
                continue

            if previousRow[colIndex - 1] == 1 and previousRow[colIndex] == 0 and previousRow[colIndex + 1] == 0:
                currentRow.append(1)
                continue

            if previousRow[colIndex - 1] == 0 and previousRow[colIndex] == 0 and previousRow[colIndex + 1] == 1:
                currentRow.append(1)
                continue

            currentRow.append(0)

        currentRow.append(0)
    
    trapCount = 0

    for row in roomTiles:
        trapCount += sum(row)
    
    return (colCount * rowCount) - trapCount


print(taskOne(inputStream))
print(taskTwo(inputStream))
