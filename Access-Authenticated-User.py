'''Access the already authenticated user's access key and secret from 
text file it is saved in. Must use Twitter-Auto_OAuth.py first'''

import tweepy
import os

#ask what user we want to access
twitter_handle = raw_input('Which user are we going to access? \n>> ')

while twitter_handle + '.txt' not in os.listdir(os.getcwd()):
    print 'Dude, enter the right file name'
    twitter_handle = raw_input('Which user are we going to access? \n>> ')
    
f = open(twitter_handle + '.txt', 'r')

#assigning variables from text file
CONSUMER_KEY = f.readline().strip()
CONSUMER_SECRET = f.readline().strip()
ACCESS_KEY = f.readline().strip()
ACCESS_SECRET = f.readline().strip()

#authorizes me to actually update status and use their account
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

print 'You are all set dude!'



