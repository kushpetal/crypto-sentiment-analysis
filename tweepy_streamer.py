from tweepy import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

import config

class TwitterStreamer():
    
    def stream_tweets(self, crypto_keywords):
        listener = StdOutListener(Stream)
        auth = OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
        auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
        stream = Stream(auth, listener)
        stream.filter(track = crypto_keywords)

class StdOutListener(StreamListener):

    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename
        
    def on_data(self, data):
        try:
            json_load = json.loads(data)
            texts = json_load['text']
            coded = texts.encode('utf-8')
            s = str(coded)
            print(s[2:-1]) #text from tweet
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))

    def on_error(self, status):
        print(status)
        pass

if __name__ == "__main__":
    crypto = ["ethereum"]
    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(crypto)
