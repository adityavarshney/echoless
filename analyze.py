# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from entity import Entity

# Instantiates a client
client = language.LanguageServiceClient()

def google_analyze_entity_sentiment(tweet, entities_map):
	document = types.Document(
	    content=tweet,
	    type=enums.Document.Type.PLAIN_TEXT)
	entities = client.analyze_entity_sentiment(document).entities
	entity_type = ('UNKNOWN', 'PERSON', 'LOCATION', 'ORGANIZATION',
                   'EVENT', 'WORK_OF_ART', 'CONSUMER_GOOD', 'OTHER')
	for entity in entities:
		name = entity.name
		entity_type = entity_type[entity.type]
		entity_info = get_entity_info(name, entity_type, entities_map)
		entity_info.increment_count()
		entity_info.increment_salience(entity.salience)
		entity_info.increment_score(entity.score)
		entity_info.increment_magnitude(entity.magnitude)

def get_entity_info(name, entity_type, entities_map):
	if name not in entities_map:
		entities_map[name] = []
	entity_info = None
	for e in entities_map[name]:
		if e['type'] == entity_type:
			return e
	entity_info = Entity(name, entity_type)
	entities_map[name].append(entity_info)
	return entity_info

def get_top_n(entities_map, n):
	return