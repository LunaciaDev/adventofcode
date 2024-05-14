inputFile = open("input")
inputStream = inputFile.read()

#Sanitizing input
inputStream = inputStream.split("\n")

def taskOne(inputStream):
    totalIndex = 0

    for room in inputStream:
        room = room.split("[")
        room[-1] = room[-1].strip("]")

        temp = room[0].split("-")
        
        room.append(int(temp[-1]))

        room[0] = "".join(temp[:-1])

        characterList = [[0, i] for i in range(26)]
        
        for character in room[0]:
            characterList[ord(character) - 97][0] += 1
        
        characterList.sort(
            key = lambda character: character[0],
            reverse = True
        )

        checkString = "".join([chr(characterList[i][1] + 97) for i in range(5)])
        if (checkString == room[1]):
            totalIndex += room[2]

    print(totalIndex)

def taskTwo(inputStream):
    for room in inputStream:
        room = room[:-7]

        roomID = int(room[-3:])
        characterWrapAmount = roomID % 26

        room = " ".join(room[:-4].split("-"))

        decryptedName = []
        
        for index in range(len(room)):
            if room[index] == " ":
                decryptedName.append(" ")
                continue
            
            newCharCode = ord(room[index]) + characterWrapAmount
            if newCharCode > 122:
                newCharCode -= 26

            decryptedName.append(chr(newCharCode))

        if ("".join(decryptedName) == "northpole object storage"): # why
            print(roomID)
            return

taskOne(inputStream)
taskTwo(inputStream)
