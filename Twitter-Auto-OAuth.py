'''Program to authenticate users for your Twitter App. Will create a text 
file with users Access Key and Access Secret for later retrieval'''

import tweepy
import webbrowser

#my keys for my specific app
CONSUMER_KEY = 'Insert your Twitter app Consumer Key'
CONSUMER_SECRET = 'Insert your Twitter app Consumer Secret'
callback_url = 'http://www.twitter.com'

#the OAuth authentication process
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth_url = auth.get_authorization_url()

#welcoming user to program and telling them whats happening
start_authorizing = raw_input('What\'s up, we are about to authorize \
the app to work with your twitter account. Hit Enter when you ready.')

#to be able to open website where user authorizes app
handle = webbrowser.get()
handle.open(auth_url)

#User will continue program once they authorized
verifier = raw_input('Hit Enter once you authorized the app! \
\n>>').strip()
auth.get_access_token(verifier)

#gets the users Access key and secret
ACCESS_KEY = auth.access_token.key
ACCESS_SECRET = auth.access_token.secret
print "ACCESS_KEY = '%s'" % ACCESS_KEY
print "ACCESS_SECRET = '%s'" % ACCESS_SECRET

#authorizes me to actually update status and use their account
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
                 
#getting user's twitter handle
twitter_handle = str(api.me().screen_name)

#creating and saving a new text file with user's access key and secret
f = open(twitter_handle + '.txt', 'w')
f.write(CONSUMER_KEY.lstrip("'").rstrip("'") + '\n')
f.write(CONSUMER_SECRET.lstrip("'").rstrip("'") + '\n')
f.write(ACCESS_KEY.lstrip("'").rstrip("'") + '\n')
f.write(ACCESS_SECRET.lstrip("'").rstrip("'") + '\n')

f.close()

ask_to_update = raw_input('Sweet, looks like we are all set \n \
You want to update your status now? Yes or no?\n>> ')

#updating user's status
if ask_to_update.lower() == 'yes':
    status = raw_input('Type your status update: \n>> ')
    api.update_status (status)
    
    #open twitter feed is user wants
    open_page = raw_input('Done! You want to see your twitter feed? \
Yes or no? \n>> ')
    if open_page.lower() == 'yes':
        handle.open('http://twitter.com/' + twitter_handle)
        