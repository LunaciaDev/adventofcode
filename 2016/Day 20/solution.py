inputFile = open("input")
inputStream = inputFile.read()

inputStream = inputStream.strip().split("\n")
ipBanList = []

for bannedRange in inputStream:
    bannedRange = bannedRange.split("-")
    ipBanList.append((int(bannedRange[0]), int(bannedRange[1])))

ipBanList.sort(key = lambda range: range[0])

def taskOne(inputStream):
    minBanned = ipBanList[0][1] + 1

    for index in range(1, len(ipBanList)):
        if ipBanList[index][0] > minBanned:
            return minBanned

        minBanned = max(minBanned, ipBanList[index][1] + 1)

def taskTwo(inputStream):
    minBanned = ipBanList[0][1] + 1
    notBannedCount = 0

    for index in range(1, len(ipBanList)):
        if ipBanList[index][0] > minBanned:
            notBannedCount += ipBanList[index][0] - minBanned

        minBanned = max(minBanned, ipBanList[index][1] + 1)
    
    return notBannedCount + max(0, 4294967295 - minBanned)

print(taskOne(inputStream)) # 22887907
print(taskTwo(inputStream)) # 109
