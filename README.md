# Search Engine

![Alt Text](https://assets2.41studio.com/uploads/monologue/post/header_image/24/search-engine.png)

building up a search-engine for a University project in the course of Algorithm of data-mining.

Scraping 60 thousands songs on Azlyrics web-site using BeautifulSoup package in python.

Then we upload them into MongoDb and we start to do the pre-processing on the data:

+ removing stopwords and all the songs that were not in english language
+ Tokenization
 
At this point we built-up the main character of the Search engine which is the *Inverted index*, creating a set of all the words in the lyrics with the stemming:

+ loving becomes love
+ baby becomes babi

So we again uploaded the vocabulary (set of all the words used in the songs) and the inverted index into another collections of MongoDb.

The structure of the inverted index is quite simple and it's this:



      "_id": {
      
          "$oid": "5a23749659ac121ffe39e932"
      
      },
      
      "love": {
      
          "id_songs": tf (term-frequency),

      }
      
Once created the inverted index, we can make the query from input (which is/are the words we are searching for!!):


  searchstring = input("Search: ")

  myset = searchstring.split()

We did the set of the query and then obviously the stemming otherwise when we are searching in the vocabulary (which is a set) it will return nothing.

From this moment we computed all the important measures we need for the cosine similarity:

1. **Idf** and **tf** of the words of the query
2. then we vectorize the query
3. we get id of the songs which contains words of the query
4. so we created the vector of the documents and we normalized it computing **idf** times **tf**

At this point we computed the cosine score to compare documents among them and we got the 10 most important.

Last step was to clusterized and make a word-cloud.
