from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

# consumer_key = 'NOT'
# consumer_secret = 'GETTING'
# access_token_key = 'MY'
# access_token_secret = 'KEYS'

consumer_key = 'viFcnMBuuVEEACYk8uHVJFxGl'
consumer_secret = 'EoDGnIUQ316VbzaMt3nfcvwj4qnhpz8RyWWgyO28LF4HMFbHTu'
access_token_key = '67738036-SM5J8ZMIqXTYkhLfcnrBphP4Y7QbUITZwZ6IWxsF0'
access_token_secret = 'FNaXS2d7JvdY4GLOMXHqWHR7iIMU10GR94GUmafBBClXn'

auth = OAuthHandler(consumer_key, consumer_secret) #OAuth object
auth.set_access_token(access_token_key, access_token_secret)

setTerms = ['kill myself', 'suicide', 'want to die', 'self-harm']
SF_BOX = [121.4900, 37.2200,  122.3100,37.5200]


class StdOutListener(StreamListener):

	def on_data(self, data):
		fhOut.write(data)
		j=json.loads(data)
		text=j["text"] #The text of the tweet
		print(text) #Print it out
		print('\n')

	def on_error(self, status):
		print("ERROR")
		print(status)


if __name__ == '__main__':
	try:
		fhOut = open("test_tweets.json","a")
		l = StdOutListener()
		stream = Stream(auth, l,timeout=30)
		stream.filter(track=setTerms, locations=SF_BOX)

	except KeyboardInterrupt:
		pass
	fhOut.close()
