inputFile = open("input")
inputStream = inputFile.read()

#sanitize input
inputStream = inputStream.split("\n")
for index in range(len(inputStream)):
    inputStream[index] = inputStream[index].replace(" -> ", " ")
    inputStream[index] = inputStream[index].split(" ")

wireSetup = dict()

#Helper functions
#Manually converting to 16-bit binary for calculation since Python doesn't do that
#Final result is obtained by int([binStr], 2)
def intToBin16(integer):
    output = ""
    while integer > 0:
        output = str(integer % 2) + output
        integer = integer // 2
    return output.zfill(16)

#Working with our binary
def NOT(binary):
    output = ""
    for number in binary:
        output = output + str(1 - int(number))
    return output.zfill(16)

def AND(binaryA, binaryB):
    output = ""
    for index in range(16):
        output = output + str(int(binaryA[index]) * int(binaryB[index]))
    return output.zfill(16)

def OR(binaryA, binaryB):
    output = ""
    for index in range(16):
        output = output + str(1 if int(binaryA[index]) + int(binaryB[index]) == 2 else int(binaryA[index]) + int(binaryB[index]))
    return output.zfill(16)

def LSHIFT(binary, pos):
    pos = int(pos, 2)
    output = ""
    for index in range(pos, 16):
        output = output + binary[index]
    for index in range(pos):
        output = output + "0"
    return output

def RSHIFT(binary, pos):
    pos = int(pos, 2)
    output = "".zfill(pos)
    for index in range(16-pos):
        output = output + binary[index]
    return output

def recursiveSolver(target):
    global wireSetup #Surely safe
    #What am I doing

    if type(wireSetup[target]) is dict:
        for slot in wireSetup[target]["slot"]:
            if slot.isnumeric(): continue #Check if the slot has a signal
            if type(wireSetup[slot]) is not dict: continue #Check if the referred wire got a signal or not
            recursiveSolver(slot)

        slot = wireSetup[target]["slot"]

        match wireSetup[target]["action"]:
            case "NOT": wireSetup[target] = NOT(wireSetup[slot[0]])
            #AND and OR can accept a signal at slot 0, so check if that is receiving a signal or a wire
            case "AND": wireSetup[target] = AND(wireSetup[slot[0]] if not slot[0].isnumeric() else slot[0], wireSetup[slot[1]])
            case "OR": wireSetup[target] = OR(wireSetup[slot[0]] if not slot[0].isnumeric() else slot[0], wireSetup[slot[1]])
            #LSHIFT and RSHIFT action always receive a signal at slot 1
            case "LSHIFT": wireSetup[target] = LSHIFT(wireSetup[slot[0]], slot[1])
            case "RSHIFT": wireSetup[target] = RSHIFT(wireSetup[slot[0]], slot[1])

    else:
        if not wireSetup[target].isnumeric():
            recursiveSolver(wireSetup[target])
            
        wireSetup[target] = wireSetup[wireSetup[target]]

def constructWireSetup(inputStream):
    global wireSetup
    for instruction in inputStream:
        match len(instruction): #Instruction size of 2 is assignment, 3 is NOT, 4 is the rest
            case 2:
                wireSetup[instruction[-1]] = intToBin16(int(instruction[0])) if instruction[0].isnumeric() else instruction[0]
            case 3:
                wireSetup[instruction[-1]] = {
                    "action": "NOT",
                    "slot": [instruction[1]]
                }
            case 4:
                wireSetup[instruction[-1]] = {
                    "action": instruction[1],
                    "slot": [intToBin16(int(instruction[0])) if instruction[0].isnumeric() else instruction[0], 
                            intToBin16(int(instruction[2])) if instruction[2].isnumeric() else instruction[2]]
                }
###

def taskOne(inputStream):
    constructWireSetup(inputStream)

    recursiveSolver("a")

    print(int(wireSetup["a"], 2)) #956

def taskTwo(inputStream):
    global wireSetup #Surely safe
    constructWireSetup(inputStream)

    wireSetup["b"] = intToBin16(956)

    recursiveSolver("a")

    print(int(wireSetup["a"], 2)) #40149


taskOne(inputStream)
taskTwo(inputStream)