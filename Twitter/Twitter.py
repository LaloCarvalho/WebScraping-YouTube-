from __future__ import absolute_import, print_function
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import datetime 

GetDataHoje = datetime.datetime.now()
GetDataHoje = str(GetDataHoje)
GetDataHoje = GetDataHoje[:10]

#Add below your keys
consumer_key=""
consumer_secret=""

access_token=""
access_token_secret=""

lista = []

class StdOutListener(StreamListener):

    def on_status(self, status):
        data = status.user.screen_name+'|||'+status.text+'|||'+str(status.created_at)
        print(data)
        lista.append(data)
        with open(r'Twitter'+GetDataHoje+'.txt', 'w', encoding="utf-8") as save:
            save.writelines(lista)
        return True 

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)´
	#track= Key word
    s = stream.filter(track=[''], languages=['pt'])  
    