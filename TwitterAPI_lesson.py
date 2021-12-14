# -*- coding: utf-8 -*-
import tweepy

# 認証に必要なキーとトークン
API_KEY = 'ORQaivdLITqo3qTvxM4Y6h4Rl'
API_SECRET = 'qmQuNTIQ9xKCjTQ2adLZQvsDK8kP5A9obwaAd77kFxOUagWg0m'
ACCESS_TOKEN = '4803016783-Sq6dcTCsfp8xLUycb5YbAxjLXlo7eN1cbAPhi94'
ACCESS_TOKEN_SECRET = 'HnWreMf51mG5PdoXaN2eWiWeIXFewILvwMYDj16F8wOLP'

# APIの認証
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# キーワードからツイートを取得
api = tweepy.API(auth)
tweets = api.search(q=['Python'], count=10)

for tweet in tweets:
    print('-----------------')
    print(tweet.text)