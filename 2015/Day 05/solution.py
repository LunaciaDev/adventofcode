inputFile = open("input")
inputStream = inputFile.read()

#Sanitizing input
inputStream = inputStream.split("\n")

def taskOne(inputStream):
    niceStringCount = 0

    for string in inputStream:
        #Check for ab, cd, pq, xy
        flag = False
        for index in range(1, len(string)):
            substr = string[index-1:index+1]
            if substr == 'ab' or substr == 'cd' or substr == 'pq' or substr == 'xy':
                flag = True
                break 
        
        if flag: continue
        
        #Check vowel and pair
        vowelCount = 0
        doubleLetter = False

        for index in range(len(string)):
            char = string[index]
            if "aeiou".count(char) == 1:
                vowelCount += 1
            if index == len(string)-1: continue
            if string[index+1] == char:
                doubleLetter = True
        
        if vowelCount > 2 and doubleLetter:
            niceStringCount += 1
    
    print(niceStringCount) #255

def taskTwo(inputStream):
    niceStringCount = 0
    
    for string in inputStream:
        ruleOne = False
        ruleTwo = False

        for index in range(len(string)-1):
            if string.count(string[index:index+2]) > 1:
                ruleOne = True

            if index < len(string)-2:
                if string[index] == string[index+2]:
                    ruleTwo = True

            if ruleOne and ruleTwo: break
        else: continue # If break didn't happen, it's naughty, and next string is checked. Does not execute if break happens.

        niceStringCount += 1

    print(niceStringCount) #55

taskOne(inputStream)
taskTwo(inputStream)
