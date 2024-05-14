inputFile = open("input")
inputStream = inputFile.read().strip().split("\n")

for index in range(len(inputStream)):
    temp = inputStream[index]
    temp = temp.split(" ")

    temp[0] = temp[0][0] + temp[1][0]
    temp.pop(1)

    inputStream[index] = temp


def swapPlace(password, leftPointer, rightPointer):
    temp = password[leftPointer]
    password[leftPointer] = password[rightPointer]
    password[rightPointer] = temp

def swapLetter(password, leftChar, rightChar):
    rp = 0
    lp = 0

    for index in range(len(password)):
        if password[index] == leftChar:
            lp = index
        
        if password[index] == rightChar:
            rp = index

    temp = password[lp]
    password[lp] = password[rp]
    password[rp] = temp

def rotate(password, amount, direction):
    amount %= len(password)

    newPassword = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    for index in range(len(password)):
        target = index + amount * direction

        if target >= len(password): target -= len(password)
        if target <= len(password) * (-1) + 1: target += len(password)

        newPassword[index] = password[target]
    
    for index in range(len(password)):
        password[index] = newPassword[index]

def reversePosition(password, leftPointer, rightpointer):
    iterator = list(reversed(password[leftPointer:rightpointer+1]))

    for index in range(leftPointer, rightpointer+1):
        password[index] = iterator[index - leftPointer]

def taskOne(inputStream):
    password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    for instruction in inputStream:
        match instruction[0]:
            case 'sp':
                swapPlace(password, int(instruction[1]), int(instruction[4]))
            
            case 'sl':
                swapLetter(password, instruction[1], instruction[4])
            
            case 'rr':
                rotate(password, int(instruction[1]), -1)

            case 'rl':
                rotate(password, int(instruction[1]), 1)
            
            case 'rb':
                rotationCount = 0

                for index in range(len(password)):
                    if password[index] == instruction[5]:
                        rotationCount += index
                        break
                
                if rotationCount >= 4:
                    rotationCount += 1
                
                rotationCount += 1
                
                rotate(password, rotationCount, -1)

            case 'rp':
                reversePosition(password, int(instruction[1]), int(instruction[3]))
            
            case 'mp':
                password.insert(int(instruction[4]), password.pop(int(instruction[1])))

    print("".join(password))

def taskTwo(inputStream):
    password = ['f', 'b', 'g', 'd', 'c', 'e', 'a', 'h']

    rotationLookupTable = [7, 7, 2, 6, 1, 5, 0, 4]

    for instruction in reversed(inputStream):
        match instruction[0]:
            case 'sp':
                swapPlace(password, int(instruction[4]), int(instruction[1]))
            
            case 'sl':
                swapLetter(password, instruction[4], instruction[1])
            
            case 'rr':
                rotate(password, int(instruction[1]), 1)

            case 'rl':
                rotate(password, int(instruction[1]), -1)
            
            case 'rb':
                for index in range(len(password)):
                    if password[index] == instruction[5]:
                        rotate(password, rotationLookupTable[index], -1)
                        break

            case 'rp':
                reversePosition(password, int(instruction[1]), int(instruction[3]))
            
            case 'mp':
                password.insert(int(instruction[1]), password.pop(int(instruction[4])))

    print("".join(password))

taskOne(inputStream)
taskTwo(inputStream)