# A twitter bot that will tweet my favoruite scriptures daily - Tweepy

# Import scriptures
# Login to twitter
# Create new tweet
# Past and Post tweet

import tweepy
import time
from autoscraper import AutoScraper

CONSUMER_KEY = 'tyHCivCLoZK7TG9WRzwGdhGiC'
CONSUMER_SECRET = 'cBvYPDY1ybqEjYP0Hz4tqmayVaUqs45OxbdMDdYJboFFNQShNe'
ACCESS_KEY = '969633595454316545-Jl9nv3MyDMGDzFATh1CaNJvvCBN8mJ7'
ACCESS_SECRET = 'iZV3U55LWJyxbfnvDfwb5Gz7yjTVyzv0BJQPOJEdGU9tr'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

#create api object
twitter_API = tweepy.API(auth)

url = 'https://www.biblestudytools.com/topical-verses/the-25-most-read-bible-verses/'

wanted_list = ["Philippians 4:13:"]

scraper = AutoScraper()
result = scraper.build(url, wanted_list)
print(result)
# twitter_API.update_status("Do not be anxious about anything, but in every situation, by prayer and petition, with thanksgiving, present your requests to God. - Philippians 4:6")
