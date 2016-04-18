from flask import Flask, request, render_template # redirect, url_for, flash
import ipdb, re
import pandas as pd
import numpy as np
from cleaning_data import clean_tweet
from flask.ext.mongokit import MongoKit
from flask.ext.mongokit import Connection
from model import Model
import cPickle as pickle


model = pickle.load(open('models/model.pkl','rb'))

con1 = Connection()

# db = client.tweets
# coll = db.thursdaytest
# coll_new = db.tweets_answered

#my local tweets testing on my desktop
db = con1.twitter
coll = db.curalate
coll_new = db.curalate2 #second database that we will be creating



def get_random_tweet():
    '''gets random tweet from DB and removes'''
    rand_int = np.random.randint(0,coll.count())
    content = coll.find().limit(-1).skip(rand_int).next()
    coll.remove({'_id':content['_id']})
    return content

def get_only_neg_tweets():
    content = get_random_tweet()
    if model.predict([content['text']])[0] == 1: #only accepts list...
        return content
    else:
        pass


def send_to_database(tweet_content, param):
    '''add user input to tweet content and add user info'''
    if param == 'Yes':
        coll_new.insert({'item': tweet_content, 'user_ans': 1 })
    else:
        coll_new.insert({'item': tweet_content, 'user_ans': param })


app = Flask(__name__)


# Homepage with form on it.
#================================================
@app.route('/')
def index():
    return render_template('read_more.html')

@app.route('/first_tweet',methods=['POST','GET'])
def next():
    for i in range(3):
        if request.method =='POST':
            tweet = get_random_tweet()
            text = tweet['text']
            content = {'text':clean_tweet(text)}
            return render_template('user_answer2.html', content=content)
        if request.method =='GET':
            return str(0)


@app.route('/display_tweet/', methods=['POST','GET'])
def display_tweet():

    '''get a bad request error when do request.form['submit']
    does somebody know the php method to fix?'''

    tweet = get_random_tweet()
    text = tweet['text']
    tweet_id = tweet['id']
    content = {'text': clean_tweet(text)}
    if request.method == 'GET':
        if request.form.get('submit') == 'yes':
            send_to_database(tweet,param='Yes')
        elif request.form.get('submit') == 'no':
            send_to_database(tweet,param='Yes')
        else:
            send_to_database(tweet,request.form.get('submit'))
        return render_template('user_answer2.html', content=content)
    elif request.method == 'POST':
        return render_template('user_answer2.html', content=content)




@app.route('/stop',methods=['POST','GET'])
def stop():
    '''thanks user and gives them option to read more'''
    return render_template('stop.html')

@app.route('/read_more',methods=['POST','GET'])
def read_more():
    '''this page should have a lot of d3 vis on suicide statistics'''
    return render_template('text_about.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
