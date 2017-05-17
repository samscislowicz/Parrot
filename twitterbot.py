#!/usr/bin/python3

'''
Twitterbot
'''
from storage.retweets import Retweet
from storage import storage
import sys
import tweepy


CONSUMER_KEY = __import__('api-token').CONSUMER_KEY
CONSUMER_SECRET = __import__('api-token').CONSUMER_SECRET
ACCESS_TOKEN_KEY = sys.argv[1]
ACCESS_TOKEN_SECRET = sys.argv[2]
KEYWORD = sys.argv[3]

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
tweets = api.search(q=KEYWORD)
for tweet in tweets:
    if not storage.check_retweet(tweet.id):
        api.retweet(tweet.id)
        add_retweet(api.me(), tweet):
        break;
