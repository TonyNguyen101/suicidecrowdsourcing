from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

consumer_key = 'NOT'
consumer_secret = 'GETTING'
access_token_key = 'MY'
access_token_secret = 'KEYS'


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
		fhOut = open("sf_tweets.json","a")
		l = StdOutListener()
		stream = Stream(auth, l,timeout=30)
		stream.filter(track=setTerms, locations=SF_BOX)

	except KeyboardInterrupt:
		pass
	fhOut.close()
