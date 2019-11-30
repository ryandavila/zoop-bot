import os
import time
import tweepy
from dotenv import load_dotenv

load_dotenv()

auth = tweepy.OAuthHandler(os.getenv('API_KEY'), os.getenv('API_SECRET'))
auth.set_access_token(os.getenv('ACCESS_TOKEN'), os.getenv('ACCESS_SECRET'))
api = tweepy.API(auth)

