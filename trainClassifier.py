# import json
# from watson_developer_cloud import NaturalLanguageClassifierV1

# # "url": "https://gateway.watsonplatform.net/natural-language-classifier/api"

# natural_language_classifier = NaturalLanguageClassifierV1(
#   username='3512f82e-31e3-4e1f-a33d-48656fa12b59',
#   password='PSFYC1IQ3Sor')

# # with open('/Users/gillianchu/Desktop/echoless/allSenatorTweetsAndScores.csv', 'rb') as training_data:
# #   classifier = natural_language_classifier.create(
# #     training_data=training_data,
# #     name='Political Spectrum Classifier',
# #     language='en'
# #   )

# # status = natural_language_classifier.status('ebd44cx231-nlc-12191')
# # print (json.dumps(status, indent=2))

# # classes = natural_language_classifier.classify('ebd44cx231-nlc-12191', 'Stock Market hits an ALL-TIME high! Unemployment lowest in 16 years! Business and manufacturing enthusiasm at highest level in decades!')
# # print(json.dumps(classes, indent=2))

# # classes = natural_language_classifier.classify('ebd44cx231-nlc-12191', 'Health care has always been about something bigger than politics: its about the character of our country.')
# # print(json.dumps(classes, indent=2))


# classes = natural_language_classifier.classify('ebd44cx231-nlc-12191', 'The landmark #ParisAgreement enters into force today—we must keep up the momentum to #ActOnClimate.')
# print(json.dumps(classes, indent=2))

# # classifiers = natural_language_classifier.list()
# # print(json.dumps(classifiers, indent=2))