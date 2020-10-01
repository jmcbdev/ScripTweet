# A twitter bot that will tweet my favoruite scriptures daily - Tweepy

# Import scriptures
# Login to twitter
# Create new tweet
# Past and Post tweet

import tweepy
import time
import random

CONSUMER_KEY = 'API key' #replace with key
CONSUMER_SECRET = 'Secret key' #replace with key
ACCESS_KEY = 'Access Token' #replace with token
ACCESS_SECRET = 'Access token secret'#replace with token
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

#create api object
twitter_API = tweepy.API(auth)

# Open text file with the text you want to tweet
with open("/Users/kudakadira/github/ScripTweet/scriptures.txt", "r") as file:
    data = file.readlines()

# Print one random line (scripture) everytime the program runs
for x in range(1):
	twitter_API.update_status(data[random.randint(0, len(data))])
# twitter_API.update_status("Do not be anxious about anything, but in every situation, by prayer and petition, with thanksgiving, present your requests to God. - Philippians 4:6")
