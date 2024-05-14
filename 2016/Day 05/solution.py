from hashlib import md5
from os import system, name
from random import randint

inputFile = open("input")
inputStream = inputFile.read()

redTextPrefix = "\033[1;38;2;231;130;132m"
greenTextPrefix = "\033[1;38;2;166;209;137m"
postfix = "\033[0m"

def taskOne(inputStream):
    inputStream = inputStream.strip()
    password = []
    postfix = 0
    hexDigest = md5(str.encode(inputStream + str(postfix)))
    hexDigest = hexDigest.hexdigest()

    while len(password) < 8:
        while hexDigest[:5] != "00000":
            postfix += 1
            hexDigest = md5(str.encode(inputStream + str(postfix)))
            hexDigest = hexDigest.hexdigest()

        password.append(hexDigest[5])
        postfix += 1
        hexDigest = md5(str.encode(inputStream + str(postfix)))
        hexDigest = hexDigest.hexdigest()
    
    print("".join(password))

def stylepointDecryption(currentDecryptArray, solvedPosition):
    if (name == "nt"):
        system('cls')
    else:
        system('clear')

    for charIndex in range(len(currentDecryptArray)):
        if (solvedPosition[charIndex]):
            print(greenTextPrefix + currentDecryptArray[charIndex] + postfix, end="")
        else:
            print(redTextPrefix + chr(randint(97, 122)) + postfix, end="")

    print()


def taskTwo(inputStream):
    # Going to go for the style point by flooding the terminal with random "decrypting" stuff
    # Could do better!

    inputStream = inputStream.strip()
    password = ['_' for _ in range(8)]
    solvedPosition = [False for _ in range(8)]
    solvedCount = 0
    postfix = 0
    hexDigest = md5(str.encode(inputStream + str(postfix)))
    hexDigest = hexDigest.hexdigest()

    while solvedCount < 8:
        while hexDigest[:5] != "00000":
            postfix += 1
            hexDigest = md5(str.encode(inputStream + str(postfix)))
            hexDigest = hexDigest.hexdigest()
            
            if randint(0, 100000) == 100000:
                stylepointDecryption(password, solvedPosition)

        if not hexDigest[5].isdigit():
            postfix += 1
            hexDigest = md5(str.encode(inputStream + str(postfix)))
            hexDigest = hexDigest.hexdigest()
            stylepointDecryption(password, solvedPosition)
            continue

        position = int(hexDigest[5])

        if position > 7:
            postfix += 1
            hexDigest = md5(str.encode(inputStream + str(postfix)))
            hexDigest = hexDigest.hexdigest()
            stylepointDecryption(password, solvedPosition)
            continue

        if solvedPosition[position]:
            postfix += 1
            hexDigest = md5(str.encode(inputStream + str(postfix)))
            hexDigest = hexDigest.hexdigest()
            stylepointDecryption(password, solvedPosition)
            continue

        password[position] = hexDigest[6]
        solvedPosition[position] = True
        postfix += 1
        solvedCount += 1
        hexDigest = md5(str.encode(inputStream + str(postfix)))
        hexDigest = hexDigest.hexdigest()
        stylepointDecryption(password, solvedPosition)

taskOne(inputStream)
taskTwo(inputStream)
