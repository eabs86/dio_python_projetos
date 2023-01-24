from typing import Any, Dict, List

import tweepy

from src.secrets import CONSUMER_SECRET, CONSUMER_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
from src.connection import tweets_collection
auth = tweepy.OAuth1UserHandler(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


def _get_tweets_timeline(client:tweepy.Client) -> List[Dict[str, Any]]:
    """

    Returns: Lista de tweet da timeline

    """

    timeline = client.get_home_timeline()
    # print(timeline[0][0]['id'])
    lista = []
    tweet_dict = {}
    for i in range(len(timeline[0])):
        tweet_dict = timeline[0][i]
        # print(tweet_dict)
        lista.append({'id': tweet_dict['id'], 'text': tweet_dict['text']})
    # print(lista)

    return lista


def recent_tweets(query:str) -> List[Dict[str, Any]]:

    client = tweepy.Client(
        consumer_key=CONSUMER_KEY,
        consumer_secret=CONSUMER_SECRET,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET
    )

    search = client.search_recent_tweets(query=query,user_auth=True)

    return [tweet for tweet in search]


def get_tweets_from_mongo() -> List[Dict[str, Any]]:
    tweets = tweets_collection.find({})
    return list(tweets)


def save_tweets_timeline() -> None:
    client = tweepy.Client(
        consumer_key=CONSUMER_KEY,
        consumer_secret=CONSUMER_SECRET,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET
    )
    tweets_items = _get_tweets_timeline(client)
    tweets_collection.insert_many(tweets_items)

