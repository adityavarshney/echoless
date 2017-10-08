from trainClassifier import natural_language_classifier

def getMLClassifier(tweet):
	result = natural_language_classifier.classify('ebd44cx231-nlc-12191', tweet)
	return result['top_class']
