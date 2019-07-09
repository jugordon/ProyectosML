#!/usr/bin/python
# -*- coding: utf-8 -*-


import tweepy as tw
import pandas as pd
import re

consumer_key= ''
consumer_secret= ''
access_token= ''
access_token_secret= ''

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)


# Define the search term and the date_since date as variables
search_words = "amlo"
date_since = "2019-06-01"



new_search = search_words + " -filter:retweets"


# Collect tweets
tweets = tw.Cursor(api.search,
              q=new_search,
              lang="es",
              since=date_since).items(350)
              
 
users_locs = [[tweet.user.screen_name,re.sub(r"http\S+", "", tweet.text)] for tweet in tweets]

tweet_text = pd.DataFrame(data=users_locs, 
                    columns=['user','text'])
                    
tweet_text.to_csv('tweets.csv',encoding='utf-8')
                    
print (tweet_text)
