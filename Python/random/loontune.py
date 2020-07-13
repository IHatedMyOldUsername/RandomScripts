import urllib.request
from bs4 import BeautifulSoup
import os

episodeList = ['01 - Horton Hatches the Egg.avi',  '10 - Much Ado About Nutting.avi',
'02 - Lights Fantastic.avi',        '11 - The Hole Idea.avi',
'03 - Fresh Airedale.avi',          '12 - Now Hear This.avi',
'04 - Chow Hound.avi',              '13 - Martian Through Georgia.avi',
'05 - The Oily American.avi',       '14 - Page Miss Glory.avi',
"06 - It's Hummer Time.avi",        '15 - Norman Normal.avi']
for i in range(1,27):
    loontunalt = urllib.request.urlopen('https://www.thetvdb.com/series/looney-tunes/seasons/dvd/' + str(i))
    soup = BeautifulSoup(loontunalt, features="lxml")
    for tabrow in soup.find_all('tr'):
        for ep in tabrow.find_all('a'):
            epDB = ep.contents[0].strip()
            for realEp in episodeList:
                if(realEp[5:][:-4] == epDB):
                    SeasonEp = str(tabrow.find('td')).strip()[4:-5]
                    SeasonEp = {'Season':SeasonEp[1:3], 'Episode':SeasonEp[4:]}
                    """
                    switch = True
                    while switch:
                        try:
                            os.rename(realEp, 'Season ' + SeasonEp['Season'] + '/Looney Tunes - s' + SeasonEp['Episode'] + 'e' + SeasonEp['Episode'])
                            switch = False
                        except FileNotFoundError:
                            os.makedirs('Season ' + SeasonEp['Season'])
                    """
                    
#To remind yourself: you were working on getting season episode data out of what you just did