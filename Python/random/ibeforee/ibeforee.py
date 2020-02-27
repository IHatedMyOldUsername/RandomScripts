import re

with open('words.txt') as words:
    win = 0
    fail = 0
    wordList = words.readlines()
    for word in wordList:
        if('cie' in word):
            fail = fail+1
        #    print(fail)
            continue
        elif('cei' in word):
            win = win+1
         #   print(win)
            continue
        elif(re.search('.ei', word)):
            fail = fail+1
          #  print(fail)
            continue
        elif(re.search('.ie', word)):
            win = win+1
          #  print(win)
            continue
    
    print("Number of words following rule: " + str(win))
    print("Number of words not following rule: " + str(fail))

    print(fail/(win+fail))
