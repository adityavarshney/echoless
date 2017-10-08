import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 \
  as Features

username = "a540517a-242d-48a7-9efd-7d508cbe0268"
password = "Z6xSAluM2q1s"

natural_language_understanding = NaturalLanguageUnderstandingV1(
  username=username,
  password=password,
  version="2017-02-27")

def analyze_tweet(tweet):
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
	    )
	  ]
	)

	print(json.dumps(response, indent=2))
