import tweepy 
from datetime import datetime 

CONSUMER_KEY = "G92FvzmRT75ZU4fkBoF2ujdYv"
CONSUMER_SECRET = "A9fQgp5jVGbpVW4LRKRSbtaiIMnz6QL26fgXwgndW6zbnKTove"
ACCESS_KEY = "1881500838-smYC3gqSND3zsYNZvc40uHZ8xntV6Mah8vuWot1"
ACCESS_SECRET = "pgYl4savm4qeXDZaj6hGXKIZHb7KvaogrVgjx02revSQa"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


tweet_test = "on {}".format(datetime.now())
api.update_status(status=tweet_test)
