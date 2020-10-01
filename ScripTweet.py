# A twitter bot that will tweet my favoruite scriptures daily - Tweepy

# Import scriptures
# Login to twitter
# Create new tweet
# Past and Post tweet

import tweepy
import time

CONSUMER_KEY = 'tyHCivCLoZK7TG9WRzwGdhGiC'
CONSUMER_SECRET = 'cBvYPDY1ybqEjYP0Hz4tqmayVaUqs45OxbdMDdYJboFFNQShNe'
ACCESS_KEY = '969633595454316545-Jl9nv3MyDMGDzFATh1CaNJvvCBN8mJ7'
ACCESS_SECRET = 'iZV3U55LWJyxbfnvDfwb5Gz7yjTVyzv0BJQPOJEdGU9tr'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

#create api object
twitter_API = tweepy.API(auth)


twitter_API.update_status("Do not be anxious about anything, but in every situation, by prayer and petition, with thanksgiving, present your requests to God. - Philippians 4:6")
