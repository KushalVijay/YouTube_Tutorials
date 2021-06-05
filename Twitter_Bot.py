"""
Tutorial:https://youtu.be/JI0xE20qok8
"""

import tweepy as twitter
import secrets
import datetime
import time

auth = twitter.OAuthHandler(secrets.API_KEY,secrets.API_SECRET_KEY)
auth.set_access_token(secrets.ACCESS_TOKEN,secrets.SECRET_ACCESS_TOKEN)
api = twitter.API(auth)

def bot(hashtags):

    while True:
        print(datetime.datetime.now())

        for hashtag in hashtags:
            for tweet in twitter.Cursor(api.search, q=hashtag, rpp=10).items(5):
                try:
                    id = dict(tweet._json)['id']
                    text = dict(tweet._json)['text']

                    api.retweet(id)
                    api.create_favorite(id)

                    print("Tweet ID:",id)
                    print("Tweet Text:",text)
                except twitter.TweepError as e:
                    print(e.reason)

        time.sleep(10)


bot(['AidCovid19RT'])

