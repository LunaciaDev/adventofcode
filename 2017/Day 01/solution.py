from math import floor

inputFile = open("input")
inputStream = inputFile.read().strip()

def taskOne(inputStream):
    captchaResult = 0
    
    for index in range(len(inputStream)-1):
        if inputStream[index] == inputStream[index+1]:
            captchaResult += int(inputStream[index])
    
    captchaResult += int(inputStream[-1]) if inputStream[-1] == inputStream[0] else 0

    print(captchaResult)

def taskTwo(inputStream):
    captchaResult = 0
    shift = int(len(inputStream)/2)
    
    for index in range(len(inputStream)):
        if inputStream[index] == inputStream[(index+shift)%len(inputStream)]:
            captchaResult += int(inputStream[index])

    print(captchaResult)

taskOne(inputStream)
taskTwo(inputStream)