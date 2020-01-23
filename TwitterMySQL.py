import tweepy
import json
from dateutil import parser
import os
import subprocess
import time
from load_twitter_mysql import connect


consumer_key = 'il7g9NsjOaMULeMYiIng5kYji'
consumer_secret = 'EYIzioECGuYkVko9oiKuY1uN5MiLB5AxURkfqVOObPpXvG0S8f'
access_token = '2561813623-2TfbLj8r3Z4U5it1lHNQLRE1dMVoj6IHrAg1XSt'
access_token_secret = 'DZ8tJ4KD1y5Lass6WWOpgoJxoJ6Efw2jxe6Pnp84zJYdU'

# Tweepy class to access Twitter API
class Streamlistener(tweepy.StreamListener):

	
	

	def on_connect(self):
		print("You are connected to the Twitter API")


	def on_error(self):
		if status_code != 200:
			print("error found")
			# returning false disconnects the stream
			return False

	"""
	This method reads in tweet data as Json
	and extracts the data we want.
	"""
	def on_data(self,data):
		
		try:
			raw_data = json.loads(data)

			if 'text' in raw_data:
				 
				username = raw_data['user']['screen_name']
				created_at = parser.parse(raw_data['created_at'])
				tweet = raw_data['text']
				retweet_count = raw_data['retweet_count']

				if raw_data['place'] is not None:
					place = raw_data['place']['country']
					print(place)
				else:
					place = None
				

				location = raw_data['user']['location']

				#insert data just collected into MySQL database
				connect(username, created_at, tweet, retweet_count, place, location)
				# print(username, created_at, tweet, retweet_count, place, location)
				# print("Tweet colleted at: {} ".format(str(created_at)))
		except Exception as e:
			print(e)


if __name__== '__main__':

	# # #Allow user input
	# track = []
	# while True:

	# 	input1  = input("what do you want to collect tweets on?: ")
	# 	track.append(input1)

	# 	input2 = input("Do you wish to enter another word? y/n ")
	# 	if input2 == 'n' or input2 == 'N':
	# 		break
	
	# print("You want to search for {}".format(track))
	# print("Initialising Connection to Twitter API....")
	# time.sleep(2)

	# authentification so we can access twitter
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api =tweepy.API(auth, wait_on_rate_limit=True)

	# create instance of Streamlistener
	listener = Streamlistener(api = api)
	stream = tweepy.Stream(auth, listener = listener)

	track = ['golf', 'masters', 'reed', 'mcilroy', 'woods']
	#track = ['nba', 'cavs', 'celtics', 'basketball']
	# choose what we want to filter by
	stream.filter(track = track, languages = ['en'])