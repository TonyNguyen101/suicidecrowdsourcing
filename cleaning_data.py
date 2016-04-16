import pandas as pd
import datetime
import re

def get_json_df(datafile):
    ''''fix trailing data...?'''
    with open(datafile, 'rb') as f:
        data = f.readlines()
    data = map(lambda x: x.rstrip(), data)
    data_json_str = "[" + ','.join(data) + "]"
    data_df = pd.read_json(data_json_str)
    return data_df


def filter_tweets(string):
    '''remove any mentions'''
    new_string = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",string).split())
    if new_string.startswith('RT') == True:
        return new_string[3::]
    else:
        return new_string

def get_english_tweets(tweet_dataframe):
    langs = []
    tweet_dataframe['language'] = 0
    for i in xrange(len(tweet_dataframe)):
        langs.append(tweet_dataframe['user'][i]['lang'])
    tweet_dataframe['language'] = langs
    return tweet_dataframe[tweet_dataframe['language']=='en']

if __name__ == '__main__':
    df = get_json_df('test_tweets.json')
    df = get_english_tweets(df)
    df['text'] = df.text.apply(filter_tweets)
    df2 = df[['id','user','text']]

    '''make data set smaller so we can pass
    through to the FE in case DB's dont work'''

    df2.to_pickle('data/test2_tweets.pkl')
