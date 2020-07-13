'''
    PATCH NOTES:
    1. Create a file titled bean.json and a file title cool.json inside of the folder with the script.
    2. Install html2json and lxml
    3. Realize this is an incredibly absurd thing to waste 5 hours doing
    4. 
'''
import praw;
import psaw;
import urllib.request;
import time;
import os;
import json;
import datetime;
from lxml import html;
import requests;
import html2json

def dlSinceScript(counter, beanLocation, beanPicture):
    with open('bean.json', 'r',) as timeStamp:
        lastPostTime = timeStamp.read();
    lastPostTime = json.loads(lastPostTime);

    searchParam = "https://api.pushshift.io/reddit/search/submission/?subreddit=BeansInThings&after=" + str(int(lastPostTime["time"]));
    urllib.request.urlretrieve(searchParam, './cool.json')
    with open('cool.json', 'r') as result:
        search = result.read();
    result = json.loads(search);
    
    for i in range(0,100):
        try:    
            print(result["data"][i]["url"]);
            urllib.request.urlretrieve(result["data"][i]["url"], beanLocation + beanPicture + str(counter));
            counter = counter + 1;
        except IndexError:
            print("Done downloading other files");
            return("Empty String");

def prawLogin():
    praw.read_only = True;
    global reddit
    reddit = praw.Reddit(client_id ='yevdGhN3nV0WNg',
            client_secret = 'Not your business',
            user_agent = 'This is the BeanBot by u/IFinallyGotReddit');

#Peter: Edit these values to your preferred settings. beanPicture must have a 0 at the end. Tally hoe.
beanLocation = '.';
beanPicture = 'beanpic0'
old_item ='https://i.redd.it/xpuwvbd9i1431.jpg';
counter = 0;
#Don't edit after this unless you know what you're doing!

def findCounterLevel():
    with open('./bean.json', 'r') as count:
        counterLevel = count.read();
    counterLevel = json.loads(counterLevel);

    return(counterLevel["counter"]);

counter = findCounterLevel();
prawLogin();
dlSinceScript(counter, beanLocation, beanPicture);

while True:
    beansub = reddit.subreddit('BeansInThings');
    for submission in beansub.new(limit=1):
        new_item = submission.url;
        if(new_item != old_item and new_item.endswith('.jpg')):
            print("Downloading File: " + new_item);
            urllib.request.urlretrieve(new_item, beanLocation + beanPicture + str(counter));
            timeOfPost = { "time":submission.created_utc, "counter":counter+1 };
            with open("bean.json", "w") as write_file:
                json.dump(timeOfPost, write_file);
            
            old_item = new_item;
            print("Done!");
    time.sleep(5);
    
