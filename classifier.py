"""
Static methods for classifying text
"""

import re
from textblob import TextBlob

class TweetClassifier(object):
    """
    Static methods for classifying text
    """

    @staticmethod
    def clean_tweet(tweet):
        """
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        """
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", \
            ' ', tweet).split())

    @staticmethod
    def get_tweet_sentiment(tweet):
        """
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        """
        # create TextBlob object of passed tweet text
        analysis = TextBlob(TweetClassifier.clean_tweet(tweet))
        # set sentiment
        return analysis.sentiment.polarity
