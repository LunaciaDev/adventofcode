inputFile = open("input")
inputStream = inputFile.read()
inputStream = inputStream.strip().split("\n")

def taskOne(inputStream):
    counter = 0

    for passphrase in inputStream:
        passphrase = passphrase.split(" ")
        foundWords = []

        for word in passphrase:
            try:
                foundWords.index(word)
            except:
                foundWords.append(word)
                continue
            
            break
        else:
            counter += 1
    
    print(counter)

def taskTwo(inputStream):
    counter = 0

    for passphrase in inputStream:
        passphrase = passphrase.split(" ")
        exactWords = []
        anagrams = []

        for word in passphrase:
            exactWordFound = True
            anagramsFound = True
            sortedWord = "".join(sorted(word))

            try: 
                exactWords.index(word)
            except:
                exactWordFound = False
                exactWords.append(word)

            try:
                anagrams.index(sortedWord)
            except:
                anagramsFound = False
                anagrams.append(sortedWord)
            
            if exactWordFound or anagramsFound:
                break
        else:
            print(passphrase)
            counter += 1
    
    print(counter)

taskOne(inputStream)
taskTwo(inputStream)
