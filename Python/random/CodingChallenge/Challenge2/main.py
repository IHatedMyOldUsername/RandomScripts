import re

def dataSeparator(inputString):
    outputList = list()
    counter = 0
    counter2 = 0
    for char in inputString:
        print(char, counter, counter2)
        if char == ' ':
            outputList.append(inputString[counter-1:counter2-1])
            counter = counter2 + 1
            counter2 = counter
        else:
            counter2 =+ 1
    return(outputList)

with open('j.in', 'r') as chin:
    refinedChin = chin.readlines()
    hands = int(refinedChin[0])

lineCount = 0
for line in refinedChin:
    dataList = dataSeparator(line)
    print(dataList)
    lineCount =+ 1
