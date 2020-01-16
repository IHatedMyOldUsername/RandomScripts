import re;

win=0
fail = 0
with open('words.txt') as words:
    wordList = words.readlines()
    for word in wordList:
        for i in range(0,len(word)+1):
            testStr = word[i:i+3]
            print(testStr)
            if(testStr == 'cie'):
                fail = fail+1
                break
            elif(testStr == 'cei'):
                win = win+1
                break
            elif(testStr[:1] != 'c'):
                if(testStr[1:2] == 'ei'):
                    fail = fail+1
                    break
                elif(testStr[1:2] == 'ie'):
                    win = win+1
                    break
    
    print("Number of words following rule: " + str(win))
    print("Number of words not following rule: " + str(fail))

    print(fail/(win+fail))
