'''import new database and query to get information on user behavior,
note this takes forever to load because of the twitter API!'''
from pymongo import MongoClient
import tweepy
import re
import cPickle as pickle
from tweepy import OAuthHandler, Stream
from model import Model

model = pickle.load(open('models/model.plk','rb'))

consumer_key = 'your'
consumer_secret = 'keys'
access_token_key = 'here'
access_token_secret = ':)'

auth = OAuthHandler(consumer_key, consumer_secret) #OAuth object
auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth)

client=MongoClient()
db = client.twitter
coll = db.tweet_two #or whatever its called



def get_user_text(userid):
    '''take userid and return list of tweets that are parsed to be fed in model'''
    text_list=[]
    for i in xrange(19):
        text_list.append(api.user_timeline(userid)[i].text)
    return text_list

def get_user_time(userid):
    times = []
    for i in xrange(19):
        times.append(api.user_timeline(userid)[i].created_at)
    return times


def score_each_tweet():
    pass


def save_data():
    pass
