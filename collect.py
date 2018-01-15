
# coding: utf-8

# Group15: Alfonso D'Amelio, Claudia Colonna, Ufuk Caliskan

# # Get the links of the songs

# In[8]:

#read data e append in a list called song
songs = []
import os
for subdir, dirs, files in os.walk('/Users/alfonsodamelio/Desktop/lyrics_collection'):
    for file in files:
        if(file.endswith(".html")):
            filepath = os.sep+file
            songs.append(filepath)


# # Save data of songs

# In[9]:

columns = ["URL", "Title", "Artist", "Lyrics"]


# In[10]:

#removing this from the stopwords we are able in the next chunk to delete all songs that are not english
from nltk.corpus import stopwords
remove = ["on", "s", "a", "d", "me", "o", "do"]
eng=stopwords.words('english')
for i in remove:
    if(i in eng):
        eng.remove(i)


# In[12]:

import codecs, json, requests
from nltk.tokenize import RegexpTokenizer
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
result = []
headers = {'content-type':'application/json'}
url = "https://api.mlab.com/api/1/databases/azlyrics/collections/songs?apiKey=5DCSMLuBf6jq5qryUUWry2yW7nk1MQzT"
#response=requests.get(url)
#response.text
k = 0
for song in songs:
    iseng = False
    f = codecs.open('/Users/alfonsodamelio/Desktop/lyrics_collection'+ song , 'r', 'utf-8')
    soup = BeautifulSoup(f.read(), "lxml")
    #soup = BeautifulSoup(open('/Users/alfonsodamelio/Downloads/lyrics_collection'+ song, 'r', encoding = 'utf-8'), "html.parser")
    lst = []
    #get the link
    lst.append('/Users/alfonsodamelio/Desktop/lyrics_collection'+ song)
    #get title
    for i in soup.find_all('h1'):
        lst.append(i.text[:-6])
    #get singer
    for j in soup.find_all('h2'):
        lst.append(j.text.split(' – ')[0])
    #get lyrics       
    for link in soup.find_all('div', {"class":"dn" ,"id":"content_h"}):
        try:
            '''tokenizer = RegexpTokenizer("[A-Z]{2,}(?![a-z])|[A-Z][a-z]+(?=[A-Z])|[\'\w\-]+")
            t = tokenizer.tokenize(link.get_text(separator = ' '))'''
            
            
            tokenizer = RegexpTokenizer(r'\w+')
            t = tokenizer.tokenize(link.get_text(separator = ' '))
            x = ''
            for element in t:
                x = x+' '+element.lower()
            lst.append(x.split()) #split word in a list
            k = 0
            for word in lst[3]: #removing not english songs
                if(word in eng):
                    k +=1
                if(k==3):
                    iseng = True
                    break

        except:
            pass
    if(iseng):
        json_string = dict(zip(columns, lst))
        result.append(json_string)
    if len(result)==50000: #append in a list 50 thousand songs
        break
    


# In[20]:

len(result)


# ### uploading data on Mongodb with Pymongo

# In[21]:

import requests
import pymongo
from pymongo import MongoClient
uri='mongodb://Alfo7:alfo11295@ds117156.mlab.com:17156/azlyrics'
client=MongoClient(uri)
db=MongoClient(uri).get_database('azlyrics')
db.authenticate('Alfo7','alfo11295')
coll=db.songs


# In[22]:

coll.insert_many(result)






