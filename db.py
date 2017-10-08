from pymongo import MongoClient
from tweets import process_friends_tweets
from analyze import populate_database
from getTrainingData import getAllTweetText
import json, bson

client = MongoClient('mongodb://foo:bar@ds013495.mlab.com:13495/echoless')
db = client['echoless']
postings = db.postings_collection

def insertdb():
	tweets = getAllTweetText()
	entities = [] # list of dictionaries with name and count
	entity_names = [] # list of dictionaries with name and count

	for tweet in tweets:
		populate_database(tweet, entities, entity_names)

	print(len(entities))
	entities = [e for e in entities if e['max_sentiment'] >= 0.1 and e['max_salience'] >= 0.2]
	print(len(entities))
	db["keywords"].insert_many(entities)

