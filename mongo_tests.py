import numpy as np
from pymongo import MongoClient
# import requests
# Initialize your app and load your pickled models.
#================================================

client = MongoClient()

db = client.tweets
coll = db.thursdaytest
coll_new = db.tweets_answered


df_ny.features[i]['properties']['name']
test_string =  'New York County, NY'

def remove_ny(stirng):
    return stirng[:-11]

def get_random_tweet():
    rand_int = np.random.randint(0,coll.count())
    content = coll.find().limit(-1).skip(rand_int).next()
    text = content['text']
    if requests.user_input == 'No':
        content['answer'] = 1
    else:
        content['answer'] = 0
    coll_new.insert(content)
    return text

def get_content_from_new_db():
    return coll_new.find_one()['text']


if __name__ == '__main__':
    print get_random_tweet()
    print '----------'
    print get_content_from_new_db()
