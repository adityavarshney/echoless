from pymongo import MongoClient
from tweets import process_friends_tweets
from analyze import google_get_entity_sentiments
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
	entities = [e for e in entities if e['max_sentiment'] >= 0.25 or e['max_salience'] >= 0.25]
	print(len(entities))
	db["keywords3"].insert_many(entities)

def populate_database(tweet, entities_list, entity_names):
	entities = google_get_entity_sentiments(tweet)
	for entity in entities:
		if '@' not in entity.name and 'http' not in entity.name and '&' not in entity.name:
			try:
				i = entity_names.index(entity.name.lower())
				entities_list[i]['count'] += 1
				entities_list[i]['max_sentiment'] = max(abs(entity.sentiment.score), entities_list[i]['max_sentiment'])
				entities_list[i]['max_salience'] = max(entity.salience, entities_list[i]['max_salience'])
			except ValueError:
				new_entity = {'name': entity.name.lower(), 'count': 1, 'max_sentiment': abs(entity.sentiment.score), 'max_salience': entity.salience}
				entities_list.append(new_entity)
				entity_names.append(entity.name.lower())

def keyword_in_db(keyword):
	results = db["keywords3"].find({"name": keyword.lower()})
	return results.count() > 0
