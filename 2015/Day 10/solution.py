inputFile = open("input")
inputStream = inputFile.read()
'''
Run Length Encoding task.

There cannot be a run length of 4 or higher since it cannot appear naturally
based from task description.
1111 for instance, should have been 41, not 1111 unless it is in the starting position
A consequence of this is that the string only consist of
characters "1", "2", "3" as well as any other character in the starting string
which in this case is only "1", "2", "3"

Without realizing this insight, it take at least one hour or more to solve the 2nd task,
totally not based from experience. At all. Probably.
'''
def solver(inputStream):
    inputStream = inputStream + " "
    index = 0
    output = ""
    stringLen = len(inputStream)-1
    while index != stringLen:
        if index < stringLen-2:
            if inputStream[index] == inputStream[index+1] and inputStream[index] == inputStream[index+2]:
                output = output + f"3{inputStream[index]}"
                index += 3
                continue
        
        if index < stringLen-1:
            if inputStream[index] == inputStream[index+1]:
                output = output + f"2{inputStream[index]}"
                index += 2
                continue
        
        output = output + f"1{inputStream[index]}"
        index += 1

    return output

def taskOne(inputStream):
    for _ in range(40):
        inputStream = solver(inputStream)
    
    print(len(inputStream))

def taskTwo(inputStream):
    for _ in range(50):
        inputStream = solver(inputStream)
    
    print(len(inputStream))

taskOne(inputStream)
taskTwo(inputStream)
