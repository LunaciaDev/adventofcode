inputFile = open("input")
temp = inputFile.read()

#a - z is 97 - 122
password = []
template = [97, 97, 98, 99, 99, 100, 101, 101] #aabccdee
for index in range(len(temp)):
    password.append(ord(temp[index]))

def passwordIncrement(password, position):
    if password[position] == 122:
        password[position] = 97
        #We aren't going to go from zzzzzzz to aaaaaaaa, right?
        passwordIncrement(password, position-1)
        return
    
    #There could be a pattern to quickly get closer to the correct password with this skip
    #through I haven't figured that out yet, so I am just slapping a random template
    #for the skip based on the problem description. Hope it works?
    if password[position] == 105 or password[position] == 111 or password[position] == 108: #iol check
        for i in range(position+1, 8):
            password[i] = template[i - position - 1]
        
        password[position] += 1
        return

    password[position] += 1

def checkPassword(password):
    for index in range(5):
        if password[index] == password[index+1] -1 and password[index] == password[index+2] -2:
            break
    else: #If the break clause didn't trigger
        return False
    
    twoPair = 0
    index = 0
    while index <= 6:
        if password[index] == password[index+1]:
            twoPair += 1
            index += 2
            continue

        index += 1

    if twoPair >= 2:
        return True

    return False

def taskOne(password):
    while not checkPassword(password):
        passwordIncrement(password, 7)
    
    for character in password:
        print(chr(character), end="")
    print()

def taskTwo(password):
    passwordIncrement(password, 7)
    while not checkPassword(password):
        passwordIncrement(password, 7)
    
    for character in password:
        print(chr(character), end="")
    print()

taskOne(password)
taskTwo(password)

