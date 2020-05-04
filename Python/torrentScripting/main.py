import bs4
import requests

def queryConv(baseString):
    final = ''
    for char in baseString:
        if char == ' ':
            final = final + '+'
            continue
        else:
            final = final + char
    print(final)
    return(final)

pbURL = 'https://thepiratebay.org/search.php?q='
toFind = input('What do you want me to find? ')
toFind = queryConv(toFind)
query = requests.get(pbURL + toFind)).text

