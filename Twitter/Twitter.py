from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from datetime import datetime
from pymongo import MongoClient
import json

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

class MyListener(StreamListener):
    def on_data(self, dados):
        try:
           tweet = json.loads(dados)
           created_at = tweet["created_at"]
           id_str = tweet["id_str"]
           text = tweet["text"]
           obj = {"created_at":created_at,"id_str":id_str,"text":text,}
           tweetind = col.insert_one(obj).inserted_id
           print (obj)
        except Exception as e:
            print(e)
        return True
		
mylistener = MyListener()
mystream = Stream(auth, listener = mylistener)

client = MongoClient('localhost', 27017)
db = client.twitterdb
col = db.tweets2

keywords = ['']

mystream.filter(track=keywords)

mystream.disconnect()