import uvicorn

from src.services import recent_tweets, get_tweets_from_mongo, save_tweets_timeline
from fastapi import FastAPI
from src.responses import TweetText


app = FastAPI()


@app.get('/timeline', response_model=list[TweetText]) #
def get_tweets():
    # tweets = get_tweets_timeline()
    return get_tweets_from_mongo()


@app.get('/recent')
def recent_seven_days(query):
    tweets = recent_tweets(query=query)
    return tweets


if __name__ == '__main__':
    save_tweets_timeline()
    uvicorn.run(app)


