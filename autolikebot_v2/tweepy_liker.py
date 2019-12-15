
import tweepy
import logging
import os


class AutoLike:
    def __init__(self, api, screen_name, count):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger()
        self.api = api
        self.screen_name = screen_name
        self.count = count
        try:
            self.tweets = api.user_timeline(screen_name=self.screen_name, count=self.count, include_rts=True,
                                            tweet_mode='extended')
        except tweepy.TweepError as e:
            self.logger.warning(e)

    def like_tweets(self):
        if self.update_tweets():
            for tweet in self.tweets:
                self.logger.info(f"Processing tweet id {tweet.id}:{os.linesep}{tweet.full_text}")
                try:
                    tweet.favorite()
                except tweepy.TweepError:
                    pass

    def update_tweets(self):
        try:
            self.tweets = self.api.user_timeline(screen_name=self.screen_name, count=self.count, include_rts=True,
                                                 tweet_mode='extended')
            return True
        except tweepy.TweepError as e:
            self.logger.warning(e)
            return False
