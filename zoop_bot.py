import os
import time
import tweepy
from dotenv import load_dotenv

load_dotenv()

auth = tweepy.OAuthHandler(os.getenv('API_KEY'), os.getenv('API_SECRET'))
auth.set_access_token(os.getenv('ACCESS_TOKEN'), os.getenv('ACCESS_SECRET'))
api = tweepy.API(auth)

LAST_ID_FILE = 'last_seen_id.txt'

def get_last_seen_id(file_name):
  f_read = open(file_name, 'r')
  last_seen_id = int(f_read.read().strip())
  f_read.close()
  return last_seen_id

def save_last_seen_id(last_seen_id, file_name):
  f_write = open(file_name, 'w')
  f_write.write(str(last_seen_id))
  f_write.close()
  return

def send_test_tweet():
  print('Sending out a fat test Tweet...')
  api.update_status('We must zoop the non-believers... I mean, test.')

send_test_tweet()