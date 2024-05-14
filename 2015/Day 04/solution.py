import hashlib as h #Python Standard Library for md5()

inputFile = open("input")
inputStream = inputFile.read()

def taskOne(inputStream):
    salt = 0
    #Salted key! :3
    while True:
        salt += 1
        if h.md5(bytes(inputStream + str(salt), encoding="utf-8")).hexdigest()[:5] == "00000":
            break
    
    print(salt)


def taskTwo(inputStream):
    salt = 0
    while True:
        salt += 1
        if h.md5(bytes(inputStream + str(salt), encoding="utf-8")).hexdigest()[:6] == "000000":
            break
    
    print(salt)

taskOne(inputStream)
taskTwo(inputStream)
