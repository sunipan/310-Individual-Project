import os
import tweepy as tw
import pandas as pd
import sys
import re


class Twitter:
    
    apiKey = 'bYT3Rkm91GV8nKSXVPXQLPr5v'
    apiSecret = 'Gvbdn8nucOtFTQbAELPrtHgRHsocWalUaM4jhojdzu91cUXvU8'
    accessToken = '2211402554-YBhFqFkxUjaHdPMbUF2CvSKvr9hrVCO2Q2Es8oC'
    accessTokenSecret = 'Sk94xjatQ8RsSHuUecHXHmcnPdY9Lo9VyX6uYVEZNjEdf'

    auth = tw.OAuthHandler(apiKey, apiSecret)
    auth.set_access_token(accessToken, accessTokenSecret)
    api = tw.API(auth, wait_on_rate_limit=True)
    userName = None

    
    def setUserName(self, userInput):
        words = userInput.lower().split(' ')
        dirtyUserName = ""
        for word in words:
            if '@' in word:
                dirtyUserName = word  #we clean the username just in case it contains bad characters
                break
        dirtyUserName = re.sub('[!@$%&*)(#-]', '', dirtyUserName)
        self.userName = self.api.get_user(dirtyUserName)
        
    def action(self, num):
        if num == '1':
            return 'Date Created: ' + self.userName.created_at.strftime("%m/%d/%Y, %H:%M:%S")
        elif num == '2':
            for status in tw.Cursor(self.api.user_timeline, id=self.userName.id, exclude_replies = True).items(1):
                return status.text + ' | Date Tweeted: ' + status.created_at.strftime("%m/%d/%Y, %H:%M:%S")
        elif num == '3':
            return 'Number of Followers: ' + str(self.userName.followers_count)
        elif num == '4':
            return 'Tweets posted & Retweeted: ' + str(self.userName.statuses_count)
        elif num == '5':
            return 'Verified Status: ' + str(self.userName.verified)
        else:
            return 'Please enter a number within the given input range (1-5)'


        
