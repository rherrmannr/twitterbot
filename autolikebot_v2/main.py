from tweepy_config import create_api
from tweepy_liker import AutoLike
import threading

if __name__ == '__main__':
    # enter the username (without '@')
    WAIT_TIME_SECONDS = 3
    MAX_TWEETS = 1
    USERNAME = ''
    ticker = threading.Event()
    autoLiker = AutoLike(create_api(), USERNAME, MAX_TWEETS)
    while not ticker.wait(WAIT_TIME_SECONDS):
        autoLiker.like_tweets()
