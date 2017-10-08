# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# Instantiates a client
client = language.LanguageServiceClient()

# Maps from entity name to a list of entity_infos with that name
# Each entity_info contains its type, count, sentiment score sum, sentiment magnitude sum, and salience sum
entities_map = {}

def google_analyze_entity_sentiment(tweet):
	document = types.Document(
	    content=tweet,
	    type=enums.Document.Type.PLAIN_TEXT)
	entities = client.analyze_entity_sentiment(document).entities
	entity_type = ('UNKNOWN', 'PERSON', 'LOCATION', 'ORGANIZATION',
                   'EVENT', 'WORK_OF_ART', 'CONSUMER_GOOD', 'OTHER')
	for entity in entities:
		name = entity.name
		entity_type = entity_type[entity.type]
		entity_info = get_entity_info(name, entity_type)
		entity_info['count'] += 1
		entity_info['salience_sum'] += entity.salience
		entity_info['score_sum'] += entity.sentiment.score
		entity_info['magnitude_sum'] += entity.sentiment.magnitude

def get_entity_info(name, entity_type):
	if name not in entities_map:
		entities_map[name] = []
	entity_info = None
	for e in entities_map[name]:
		if e['type'] == entity_type:
			return e
	entity_info = {'type': entity_type, 'count': 0, 'salience_sum': 0, 'score_sum': 0, 'magnitude_sum': 0}
	entities_map[name].append(entity_info)
	return entity_info

