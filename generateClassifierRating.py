import json
from watson_developer_cloud import NaturalLanguageClassifierV1

natural_language_classifier = NaturalLanguageClassifierV1(
  username='3512f82e-31e3-4e1f-a33d-48656fa12b59',
  password='PSFYC1IQ3Sor')

def getMLClassifier(tweet):
	result = natural_language_classifier.classify('ebd44cx231-nlc-12191', tweet)
	return result['top_class']
