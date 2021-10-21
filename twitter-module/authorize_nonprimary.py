# Kennedy C. Ezumah
# April 9, 2021
# Source Code thanks to Dennis Gorbachev on GitHub: https://gist.github.com/hezhao/4772180

# NOTES:
# The purpose of this module is to authorize the integration of a Twitter Application
# with a non-primary Twitter account.
# A non-primary Twitter account is any Twitter account other than the Twitter Developer
# account used to build the application.
# This module retrieves the non-primary account's unique access_key and access_token
# and saves it in a secure file.
# A one-time, manual operation will be required to complete this procedure.

import json
import os
import tweepy
import twython

# load credentials from a separate "twitter_api_credentials" .json file for modularity and security
# make sure the file is in the same directory
with open("twitter_api_credentials") as f:
   credentials = json.load(f)

consumer_key = credentials["API_KEY"]
consumer_secret = credentials["API_SECRET"]

# set call-back parameter to 'oob' to enable PIN-authentification
auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback = 'oob')

# prompt user to open url, log in, and authorize access to retrieve PIN code
auth_url = auth.get_authorization_url()
print("Visit this url to retrieve your PIN: '%s'" % auth_url)

# ask user to verify the PIN generated in browser
verifier = input('PIN: ').strip()
auth.get_access_token(verifier)
print('ACCESS_KEY = "%s"' % auth.access_token)
print('ACCESS_SECRET = "%s"' % auth.access_token_secret)

# save access_key and access_secret to the credentials.json file
with open("twitter_api_credentials", 'w') as json_file:
   credentials["ACCESS_KEY"] = str(auth.access_token)
   credentials["ACCESS_SECRET"] = str(auth.access_token_secret)
   json.dump(credentials, json_file)

# authenticate and retrieve user name
auth.set_access_token(auth.access_token, auth.access_token_secret)
api = tweepy.API(auth)
username = api.me().name
print('Your APP is ready to post to this Twitter account: ' + username)
