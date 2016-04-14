import pandas as pd
import datetime


def get_json_df(datafile):
    with open(datafile, 'rb') as f:
        data = f.readlines()

    data = map(lambda x: x.rstrip(), data)
    data_json_str = "[" + ','.join(data) + "]"
    data_df = pd.read_json(data_json_str)
    return data_df

if __name__ == '__main__':
    df = get_json_df('suicide_tweets.json')
    df2 = df[['id','user','text']]
    df2.to_pickle('data/%d_tweets.pkl') %(str(datetime.datetime.now().date))
