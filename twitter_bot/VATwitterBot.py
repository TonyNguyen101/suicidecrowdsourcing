import os
import re
import time
import datetime
from collections import defaultdict, namedtuple

import pandas as pd
import numpy as np

import tweepy

##BOT KEYS
consumer_key = os.getenv('consumer_key')
consumer_secret = os.getenv('consumer_secret')
access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#BOT_SCREEN_NAME = 'vaTestBot'

def parse_user(twitter_handle):
    '''
    twitter_handle: either twitter ID or screen_name
    '''
    
    user = api.get_user(twitter_handle)
    return user.id, user.screen_name, user.description #, user.status ##User status is the last tweet made

#Generate the table to store our data
def generate_df():
    df = pd.DataFrame(columns=['agree_to_survey','is_veteran','has_ptsd','knows_others','screen_name','description'])
    df.index.name = 'user_id'
    return df

def update_df():
    '''
    Updates df to add new friends **There is another python script that automatically adds friends
    '''
    friends_ids = set(api.friends_ids())
    
    #Generate user_id rows
    for f in friends_ids:
        if f not in df.index:
            user_id, screen_name, user_description = parse_user(f)
            df.loc[user_id] = [None, None, None, None, screen_name, user_description]

#Check for responses by generating the conversations
Msg = namedtuple('Msg', field_names = ['user', 'datetime', 'text' ])

def collect_msgs():
    conversations = defaultdict(list)

    sent_msgs = api.sent_direct_messages()
    response_msgs = api.direct_messages()

    for m in sent_msgs:
        conversations[m.recipient_screen_name].append(Msg(m.sender_screen_name, m.created_at, m.text))

    for m in response_msgs:
        conversations[m.sender_screen_name].append(Msg(m.sender_screen_name, m.created_at, m.text))
    
    return conversations

q = {}
    
q[0] = '''
        Hello! Thanks for following us. We are trying to build a platform that will ultimately allow us to detect mental illness through text analytics.
        Could you please provide some basic information? (yes/no)
        '''
q[1] = 'Are you a veteran? (yes/no)'
        
q[2] = 'Have you ever had symptoms associated with PTSD such as depression or suicidal thoughts? (yes/no)'
        
q[3] = 'Do you know someone who may show signs of PTSD? (yes/no)'
    
q[-1] = '''Thanks. We would be very grateful if you retweet our message to reach more people.
    If you have some time, please check out our website:  XXXXXXXXXXX.XXX'''

def ask_question(screen_name, question_number = 0):
    '''
    Utilizes the twitter API to ask a specific user a question for our survey
    '''
    try:
        api.send_direct_message(screen_name, text = q[question_number])
    except:
        print 'Error'
        pass


#Check if we receive an acceptable response
acceptable_responses = set(['yes','no','y','n'])
def check_response(response):
    if response.lower() in acceptable_responses:
        return response.lower()

def parse_msg(conversation, target_user):
    '''
    Input is list of sorted (sender, datetime, txt) 
    '''
    conversation = sorted(conversation, key=lambda x: x[1])
    
    print conversation[-1]
    
    if conversation[-1].user == target_user: #Only parse of the last msg was sent by the person
        idx_last_bot_msg = np.max([idx for idx, msgs in enumerate(conversation) if msgs.user != target_user])
        last_bot_msg = conversation[idx_last_bot_msg].text
        person_response = check_response(conversation[idx_last_bot_msg + 1].text)
        
        print last_bot_msg
        
        if person_response:
            if 'Thanks for following us.' in last_bot_msg:
                if person_response == 'yes':
                    df.loc[df.screen_name == target_user, 'agree_to_survey'] = person_response
                    ask_question(target_user, 1)
                else:
                    df.loc[df.screen_name == target_user, df.columns[:4]] = ['NaN','NaN','NaN','NaN']
                    ask_question(target_user, -1)
            elif 'Are you a veteran?' in last_bot_msg:
                df.loc[df.screen_name == target_user, 'is_veteran'] = person_response
                ask_question(target_user, 2)
            elif 'you ever had symptoms associated with PTSD' in last_bot_msg:
                df.loc[df.screen_name == target_user, 'has_ptsd'] = person_response
                ask_question(target_user, 3)
            elif 'know someone who may show signs of PTSD?' in last_bot_msg:
                df.loc[df.screen_name == target_user, 'knows_others'] = person_response
                ask_question(target_user, -1)
        else:
            if last_bot_msg not in q.values():
                ask_question(target_user) #This starts the questions again
            
            
def initialize_conversations():
    for new_friend in df.screen_name[df.agree_to_survey.isnull()][:5]:
        if new_friend not in conversations.keys():
            ask_question(new_friend)

df = generate_df()
update_df()
conversations = collect_msgs()
initialize_conversations()

while(True):
    conversations = collect_msgs()
    
    for target_user, conversation in conversations.iteritems():
        parse_msg(conversation, target_user)
        
    update_df()
    initialize_conversations()
    
    df.to_csv('./twitter_survey.csv')
    
    time.sleep(30)