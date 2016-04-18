
#Updates the twitter bot by adding new followers and updating the infographic using images in the 
#Infographic folder and text in tweet_status_update.txt

import os
import sys
import time
import random

import tweepy

UPDATE_INVERVAL = 7200
INFOGRAPHIC_DIR = '../data/Infographics/'

##BOT KEYS
consumer_key = os.getenv('consumer_key')
consumer_secret = os.getenv('consumer_secret')
access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def add_followers_as_friends():
    '''
    Converting followers to friends allows for direct messaging.
    This works assuming that they are under the API Limit(200?). Will expand on later.
    '''
    followers_ids = api.followers_ids() #People following me [only Ids]
    friends_ids = set(api.friends_ids())
    
    for follower_id in followers_ids:
        if follower_id not in friends_ids:
            try:
                api.create_friendship(follower_id)
            except TwitterError:
                continue


infographic_files = os.listdir(INFOGRAPHIC_DIR)

with open('./twitter_status_updates.txt') as f:
    twitter_msgs = f.readlines()

while(True):
    add_followers_as_friends()
    tweet_img = INFOGRAPHIC_DIR + random.choice(infographic_files)
    tweet_msg = random.choice(twitter_msgs)
    api.update_with_media(tweet_img, status = tweet_msg)
    time.sleep(UPDATE_INVERVAL)