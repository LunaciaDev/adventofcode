inputFile = open("input")
inputStream = inputFile.read()

#Sanitizing input
inputStream = inputStream.split("\n")

def taskOne(inputStream):
    codeSize = 0
    memorySize = 0

    for string in inputStream:
        #Error cases that have happened:
        #\\x..(caught both \\ and \x..)
        #\\" (end of string, caught both \\ and \")
        #these could have been easily avoided if I delete as I find matches right off the bat
        codeSize += len(string)
        memorySize += len(string) - 2 - string.count(r"\\")
        string = string.replace(r"\\", "", -1)
        memorySize -= string.count(r"\"")
        string = string.replace(r"\"", "", -1)

        for index in range(1, len(string)-3):
            if string[index] == "\\" and string[index+1] == "x":
                #\x is not a valid escape sequence,
                #no need to check if the last two char is hexadecimal
                memorySize -= 3

    print(codeSize - memorySize) #1371

def taskTwo(inputStream):
    codeSize = 0
    encodeSize = 0

    for string in inputStream:
        codeSize += len(string)
        encodeSize += len(string) + 4 + 2*string.count(r"\\")
        string = string.replace(r"\\", "", -1)
        encodeSize += 2*string.count(r"\"")
        string = string.replace(r"\"", "", -1)

        for index in range(1, len(string)-3):
            if string[index] == "\\" and string[index+1] == "x":
                encodeSize += 1

    print(encodeSize - codeSize) #2117

taskOne(inputStream)
taskTwo(inputStream)
