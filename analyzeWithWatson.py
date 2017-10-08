import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1, NaturalLanguageClassifierV1
import watson_developer_cloud.natural_language_understanding.features.v1 \
  as Features

username = "a540517a-242d-48a7-9efd-7d508cbe0268"
password = "Z6xSAluM2q1s"

natural_language_understanding = NaturalLanguageUnderstandingV1(
  username=username,
  password=password,
  version="2017-02-27")

natural_language_classifier = NaturalLanguageClassifierV1(
  username=username,
  password=password)

# with open('../resources/weather_data_train.csv', 'rb') as training_data:
#   classifier = natural_language_classifier.create(
#     training_data=training_data,
#     name='Politics Training',
#     language='en'
#   )

def analyze_tweet(tweet):

	# if len(tweet) < 70:
	# 	classify_language(tweet)
	# else:
	# 	understand_language(tweet)
	understand_language(tweet)


def understand_language(tweet):
	print(tweet)
	response = natural_language_understanding.analyze(
	  text=tweet,
	  features=[
	    Features.Entities(
	      sentiment=True,
	      limit=3
	    ),
	    Features.Concepts(
	      limit=3
	    ),
	    Features.Keywords(
	      sentiment=True,
	      limit=3
	    ),
	    Features.Keywords(
	    	emotion=True,
	    	sentiment=True,
	    	limit=3
	    ),
	    Features.Categories()
	  ]
	)
	# json.dumps({key: value, key2 : value2, ...}, )
	print(json.dumps(response, indent=2))
	return response

def classify_language(tweet):
	return

analyze_tweet('communism is awesome! i hate capitalism and the US is stupid')