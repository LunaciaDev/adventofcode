inputFile = open("input")
inputStream = inputFile.read()

#Sanitizing input
inputStream = inputStream.split("\n")

def taskOne(inputStream):
    validIPCount = 0

    for ip in inputStream:
        isValid = False
        isInBracket = False
        ipLength = len(ip)
        index = 0

        while index + 3 < ipLength:
            if isValid and not isInBracket:
                while index + 3 < ipLength:
                    if ip[index] == "[":
                        index += 1
                        isInBracket = True
                        break
                    index += 1
                
                if index + 3 >= ipLength: break

            if ip[index] == "[":
                index += 1
                isInBracket = True
                continue

            if ip[index + 3] == "]":
                index += 4
                isInBracket = False
                continue

            if isInBracket:
                if ip[index] == ip[index+3] and ip[index+1] == ip[index+2] and ip[index] != ip[index+1]:
                    break

            else:
                if ip[index] == ip[index+3] and ip[index+1] == ip[index+2] and ip[index] != ip[index+1]:
                    isValid = True
                    index += 4
                    continue
                
            index += 1
        
        if index+3 < ipLength: continue
        if not isValid: continue
        
        validIPCount += 1
    
    print(validIPCount) # 118

def taskTwo(inputStream):
    validIPCount = 0

    for ip in inputStream:
        tripletOutsideBracket = []
        tripletInsideBracket = []
        isInBracket = False
        ipLen = len(ip) - 1
        index = 0

        while index + 2 <= ipLen:
            if ip[index] == "[":
                index += 1
                isInBracket = True
                continue

            if ip[index + 2] == "]":
                index += 3
                isInBracket = False
                continue

            if ip[index] == ip[index+2] and ip[index] != ip[index+1]:
                if isInBracket:
                    tripletInsideBracket.append(ip[index:index+3])
                else:
                    tripletOutsideBracket.append(ip[index:index+3])

            index += 1
        
        for triplet in tripletOutsideBracket:
            equivalentTriplet = f"{triplet[1]}{triplet[0]}{triplet[1]}"
            try:
                tripletInsideBracket.index(equivalentTriplet)
            except:
                continue

            validIPCount += 1
            break

    print(validIPCount) # 260

taskOne(inputStream)
taskTwo(inputStream)
