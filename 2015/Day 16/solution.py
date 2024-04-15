inputFile = open("input")
inputStream = inputFile.read()

propertyID = {
    "children": 0,
    "cats": 1,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 4,
    "vizslas": 5,
    "goldfish": 6,
    "trees": 7,
    "cars": 8,
    "perfumes": 9
}

sueProperties = [[-1 for _ in range(11)] for _ in range(500)]

#Sanitizing input
inputStream = inputStream.split("\n")
index = 0
for line in inputStream:
    line = line.split(" ")
    sueProperties[index][-1] = index+1
    sueProperties[index][propertyID[line[2].strip(":")]] = int(line[3].strip(","))
    sueProperties[index][propertyID[line[4].strip(":")]] = int(line[5].strip(","))
    sueProperties[index][propertyID[line[6].strip(":")]] = int(line[7])
    index += 1

properties = [ 3,  7,  2,  3,  0,  0,  5,  3,  2,  1]

def taskOne(inputStream):
    def sueSearch(): 
        for sue in sueProperties:
            for index in range(10):
                if sue[index] == -1: continue
                if sue[index] != properties[index]: break
            else: #only run if break didn't trigger
                return sue[-1]
    
    print(sueSearch()) #103

def taskTwo(inputStream):
    def sueSearch(): 
        for sue in sueProperties:
            for index in range(10):
                if sue[index] == -1: continue
                match index:
                    case 1|7:
                        if sue[index] <= properties[index]: break
                    case 3|6:
                        if sue[index] >= properties[index]: break
                    case _:
                        if sue[index] != properties[index]: break

            else: #only run if break didn't trigger
                return sue[-1]
            
    
    print(sueSearch()) #103

taskOne(inputStream)
taskTwo(inputStream)
