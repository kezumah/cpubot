# Written by Kennedy C. Ezumah
# April 10, 2021
# This module is used to make a tweet on behalf of an authorized Twitter account (See README for more on authorization)
# Thanks to https://2017.compciv.org/guide/topics/python-nonstandard-libraries/twython-guide/twitter-twython-app-auth.html for walkthrough on authentication
# See README file for full documentation

import sys
import json
from twython import Twython
 
# create class
class Twitter_Bot:

    def __init__(self, message = "This is a default tweet"):
        self.message = message
        
    def tweet(self, message):
 
        with open("twitter_api_credentials") as f:
            credentials = json.load(f)
        
        # load security credentials from a separate .json file for modularity and security
        apiKey = credentials["API_KEY"] 
        apiSecret = credentials["API_SECRET"]
        accessToken = credentials["ACCESS_KEY"]
        accessTokenSecret = credentials["ACCESS_SECRET"]
    
        api = Twython(apiKey, apiSecret, accessToken, accessTokenSecret)
        self.message = message
        
        # Include an exception statement to catch and display any errors that may be generated without crashing the main module
        # This allows the main module to continue executing even if a fatal error is encountered in this program
        try:
            api.update_status(status = self.message)
            return ("Tweeted: " + self.message)
        except Exception as e:
            return ("TWITTER ERROR MESSAGE ENCOUNTERED: %s" % e)
        

