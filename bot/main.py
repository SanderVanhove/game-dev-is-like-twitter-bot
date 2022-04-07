import time

from content import get_tweet_content
from twitter import tweet

while True:
    tweet(get_tweet_content())
    time.sleep(5 * 60)

