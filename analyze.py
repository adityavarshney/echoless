# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

from entity import Entity
# from db import keyword_in_db
from queue import PriorityQueue

# Instantiates a client
client = language.LanguageServiceClient()

def google_get_entity_sentiments(tweet):
	document = types.Document(
	    content=tweet,
	    type=enums.Document.Type.PLAIN_TEXT)
	entities = client.analyze_entity_sentiment(document).entities
	return entities

def google_analyze_entity_sentiment(entity, entities_map):
	entity_types = ('UNKNOWN', 'PERSON', 'LOCATION', 'ORGANIZATION',
                   'EVENT', 'WORK_OF_ART', 'CONSUMER_GOOD', 'OTHER')
	name = entity.name
	entity_type = entity_types[entity.type]
	entity_info = get_entity_info(name, entity_type, entities_map)
	entity_info.increment_count()
	entity_info.increment_salience(entity.salience)
	entity_info.increment_score(entity.sentiment.score)
	entity_info.increment_magnitude(entity.sentiment.magnitude)

def get_entity_info(name, entity_type, entities_map):
	if name not in entities_map:
		entities_map[name] = []
	entity_info = None
	for e in entities_map[name]:
		if e.type == entity_type:
			return e
	entity_info = Entity(name, entity_type)
	entities_map[name].append(entity_info)
	return entity_info

def get_top_n(entities_map, n):
	q = PriorityQueue()
	for name in entities_map:
		for e in entities_map[name]:
			if '@' not in e.name and 'http' not in e.name and e.score_sum != 0:
				q.put(e)
	ret = []
	for i in range(n):
		if q.empty():
			break
		ret.append(q.get())
	return ret


