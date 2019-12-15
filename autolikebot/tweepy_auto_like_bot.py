from tweepy_config import create_api
from tweepy import TweepError
import threading
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def like_tweets(api, user):
    # count = 1, only like the last one..
    try:
        tweets = api.user_timeline(screen_name=user, count=1, include_rts=True, tweet_mode='extended')
        tweet = tweets[0]

        logger.info(f"Processing tweet id {tweet.id}:{os.linesep}{tweet.full_text}")
        tweet.favorite()

    except TweepError as e:
        logger.warning(e)


if __name__ == '__main__':
    # enter the username (without '@')
    user = ''
    WAIT_TIME_SECONDS = 5
    ticker = threading.Event()
    my_api = create_api(logger)
    while not ticker.wait(WAIT_TIME_SECONDS):
        like_tweets(api=my_api, user=user)
