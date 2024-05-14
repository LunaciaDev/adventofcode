import math as m

inputFile = open("input")
inputStream = inputFile.read()

#Sanitizing input
inputStream = int(inputStream)

def taskOne(inputStream):
    for houseAddress in range(1, inputStream+1):
        presentCount = 0
        divisorList = []

        for i in range(1, m.floor(m.sqrt(houseAddress))+1):
            if houseAddress % i == 0:
                presentCount += i * 10
                divisorList.append(i)

        if m.ceil(m.sqrt(houseAddress)) == divisorList[-1]:
            divisorList.pop()
        
        for divisor in divisorList:
            presentCount += houseAddress // divisor * 10

        if presentCount > inputStream:
            print(houseAddress)
            break

def taskTwo(inputStream):
    for houseAddress in range(1, inputStream+1):
        presentCount = 0
        divisorList = []

        for i in range(1, m.floor(m.sqrt(houseAddress))+1):
            if houseAddress % i == 0:
                if houseAddress // i <= 50:
                    presentCount += i * 11
                divisorList.append(i)

        if m.ceil(m.sqrt(houseAddress)) == divisorList[-1]:
            divisorList.pop()
        
        for divisor in divisorList:
            if houseAddress // (houseAddress // divisor) <= 50:
                presentCount += houseAddress // divisor * 11

        if presentCount > inputStream:
            print(houseAddress)
            break


taskOne(inputStream)
taskTwo(inputStream)