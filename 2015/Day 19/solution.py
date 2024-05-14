inputFile = open("input")
inputStream = inputFile.read()

replacements = {}

#Sanitizing input
inputStream = inputStream.split("\n")
for line in inputStream:
    if line.strip() == "-": break

    line = line.strip().split(" ")

    if replacements.get(line[0]) == None:
        replacements[line[0]] = [line[2]]
        continue

    replacements[line[0]].append(line[2])

inputStream = inputStream[-1].strip()

def taskOne(inputStream):
    uniqueMolecules = {}

    for key in replacements:
        index = 0

        while True:
            index = inputStream.find(key, index, len(inputStream))

            if index == -1: break

            for replacement in replacements[key]:
                if uniqueMolecules.get(inputStream[:index] + replacement + inputStream[index+len(key):]) == None:
                    uniqueMolecules[inputStream[:index] + replacement + inputStream[index+len(key):]] = 1  

            index += 1

    print(len(uniqueMolecules.keys()))

'''
Let's work on a smaller input:
SiRnSiAlYSiAlYSiAlAr

Reducing this take these step:
SiAl; SiAl; SiAl; SiRnFYFYFAr.

Rn and Ar always go in pair.
Reducing Rn - Ar pair is the same as one normal reduction step - AB -> X vs ARn...Ar -> X.
Reducing k molecule take k-1 step.
You can only reduce Y by reducing the Rn - Ar pair containing it.
You can only reduce Rn - Ar pair that doesn't have Y by reducing the content down to one single molecule.
Say, an 8 element Rn - Ar pair that doesn't have Y would take 8 step.
However, same element count, but with 2 Y take only 4 step.
8 - 2*2 = 4?
So the amount of step taken to reduce k molecule is k - (Rn, Ar count) - (Y count)*2 - 1?
'''

def taskTwo(inputStream):
    moleculeCount = -1

    for index in range(len(inputStream)):
        char = inputStream[index]

        if char.isupper():
            moleculeCount += 1
        
        if char == "Y":
            moleculeCount -= 2
            continue
        
        if char == "R":
            moleculeCount -= 1

        if char == "A":
            if inputStream[index+1] == "r":
                moleculeCount -= 1        

    print(moleculeCount)

taskOne(inputStream)
taskTwo(inputStream)