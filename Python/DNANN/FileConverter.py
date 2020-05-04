with open("GMallboth.pgn") as dirtyFile:
    dirtyLines = dirtyFile.readlines()

cleanLines = []
farSig = False
i = 0
for line in dirtyLines:
    if("Result" in line and ("1-0" in line or "0-1" in line)):
        result = line[9:12]
        farSig = True
    if("1." in line and farSig):
        farSig = False
        cleanLine = [line,result]
        cleanLines.append(cleanLine)

with open('endResultList.txt', 'a') as outFile:
    outFile.write(str(cleanLines))

