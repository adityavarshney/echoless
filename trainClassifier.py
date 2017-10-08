import json
from watson_developer_cloud import NaturalLanguageClassifierV1

# "url": "https://gateway.watsonplatform.net/natural-language-classifier/api"

natural_language_classifier = NaturalLanguageClassifierV1(
  username='3512f82e-31e3-4e1f-a33d-48656fa12b59',
  password='PSFYC1IQ3Sor')

with open('/Users/gillianchu/Desktop/echoless/allSenatorTweetsAndScores.csv', 'rb') as training_data:
  classifier = natural_language_classifier.create(
    training_data=training_data,
    name='My Political Spectrum Classfier',
    language='en'
  )
print(json.dumps(classifier, indent=2))

