from flask import Flask, request, render_template, redirect, url_for
import ipdb, re
# from model import Model
import cPickle as pickle
import pandas as pd
import numpy as np
from pymongo import MongoClient
from cleaning_data import clean_tweet


# model = pickle.load(open('models/model.pkl','rb'))


client = MongoClient()
db = client.tweets
coll = db.thursdaytest

def get_random_tweet():
    rand_int = np.random.randint(0,coll.count())
    text = db.find().limit(-1).skip(rand_int).mext()['text']
    return text

app = Flask(__name__)

def return_tweet():
    '''return the text content tweet that we had
    indexed and also deletes it from the database'''

    data = pd.read_pickle('data/thursday414_tweets.pkl')
    index = np.random.randint(1,len(data))

    '''needs to be fixed for items that aren't contained in axis'''

    target_data = data.iloc[index]
    # data = data.drop(index)

    '''drop the data before sending it back'''

    # data.to_pickle('data/tweetdata.pkl')
    return target_data

# Homepage with form on it.
#================================================
@app.route('/')
def index():
    return render_template('read_more.html')


@app.route('/first_tweet',methods=['POST','GET'])
def next():
    for i in range(3):
        if request.method =='POST':
            tweet = return_tweet()
            text = tweet['text']
            content = {'text':clean_tweet(text)}
            return render_template('user_answer2.html', content=content)
        if request.method =='GET':
            return str(0)

@app.route('/display_tweet', methods=['POST','GET'])
def display_tweet():

    '''ajax requests need fixing'''

    if request.method =='GET':
        tweet = return_tweet()
        text = tweet['text']
        content = {'text': clean_tweet(text)}
        return render_template('user_answer2.html', content=content)
    if request.method =='POST':
        return str(0)

@app.route('/stop',methods=['POST','GET'])
def stop():

    '''thanks user and gives them option to read more'''

    return render_template('stop.html')

@app.route('/read_more',methods=['POST','GET'])
def read_more():

    '''this page should have a lot of d3 vis on suicide statistics'''

    return render_template('donut.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
