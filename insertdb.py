from pymongo import MongoClient
from tweets import process_friends_tweets
import json, bson
# from pymongo import DBObject 
# from pymongo import JSON 

client = MongoClient('mongodb://foo:bar@ds013495.mlab.com:13495/echoless')
db = client['echoless']
postings = db.postings_collection


db["_test2"].insert_many(process_friends_tweets())

#result = db.tweets.insert_many(process_friends_tweets())
# print(db["_test"].find_one())
# hashtags
# id
# retweet_count
# retweet_user (optional)
# user_id
# text
# media (optional): 
# 	url/ type 