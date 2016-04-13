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

	#This function gets called every time a new tweet is received on the stream
	def on_data(self, data):
		#Just write data to one line in the file
		fhOut.write(data)

		#Convert the data to a json object (shouldn't do this in production; might slow down and miss tweets)
		j=json.loads(data)

		#See Twitter reference for what fields are included -- https://dev.twitter.com/docs/platform-objects/tweets
		text=j["text"] #The text of the tweet
		print(text) #Print it out
		print('\n')

	def on_error(self, status):
		print("ERROR")
		print(status)


if __name__ == '__main__':
	try:
		#Create a file to store output. "a" means append (add on to previous file)
		fhOut = open("sf_tweets.json","a")

		#Create the listener
		l = StdOutListener()

		#Connect to the Twitter stream
		stream = Stream(auth, l,timeout=30)

		#Terms to track
		stream.filter(track=setTerms, locations=SF_BOX)

		#Alternatively, location box  for geotagged tweets
		#stream.filter(locations=[-0.530, 51.322, 0.231, 51.707])

	except KeyboardInterrupt:
		#User pressed ctrl+c -- get ready to exit the program
		pass

	#Close the
	fhOut.close()
