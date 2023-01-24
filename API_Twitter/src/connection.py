from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017/')

db = client.api_twitter

tweets_collection = db.tweets