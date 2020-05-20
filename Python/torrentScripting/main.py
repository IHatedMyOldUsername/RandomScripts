import bs4
from requests_html import HTMLSession
from selenium import webdriver
from tpb import TPB
from tpb import CATEGORIES, ORDERS

def queryConv(baseString):
    final = ''
    for char in baseString:
        if char == ' ':
            final = final + '+'
            continue
        else:
            final = final + char
    print(final)
    return('http://pirate-bay.net/search?q=' + final)

toFind = input('What do you want me to find? ')
toFind = queryConv(toFind)


elements = cleanQuery.find_all('tr')
print(elements)
