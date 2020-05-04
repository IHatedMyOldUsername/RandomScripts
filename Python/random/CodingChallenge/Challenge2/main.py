import re

def dataSeparator(inputString):
    outputString = ''
    counter = 0
    counter2 = 0
    for char in inputString:
        if char == ' ':
            pass;
        else:
            outputString = outputString + char
    return(outputString)

with open('j.in', 'r') as chin:
    refinedChin = chin.readlines()
    hands = int(refinedChin[0])

lineCount = 0
for line in refinedChin:
    dataList = dataSeparator(line)
    print(dataList)
    lineCount =+ 1
