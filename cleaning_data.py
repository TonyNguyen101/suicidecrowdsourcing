import pandas as pd
import datetime


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
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",string).split())

if __name__ == '__main__':
    df = get_json_df('suicide_tweets.json')
    df2 = df[['id','user','text']]

    '''make data set smaller so we can pass
    through to the FE in case DB's dont work'''

    df2.to_pickle('data/%d_tweets.pkl') %(str(datetime.datetime.now().date))
