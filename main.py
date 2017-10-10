from flask import Flask, render_template, redirect, url_for, request, make_response
app = Flask(__name__)

from tweets import process_friends_tweets, process_user_tweets
from analyze import google_get_entity_sentiments, google_analyze_entity_sentiment, get_top_n
from db import keyword_in_db
from generateClassifierRating import getMLClassifier

import json

@app.route('/')
def hello():
	return render_template('index.html')

@app.route('/no', methods=['POST'])
def test():
	username = request.form['username']
	return username

@app.route("/keywords", methods=['POST'])
def sendKeywords():
	username = request.form['username']
	# print("Getting friends' tweets...")
	print(username)
	# tweets = process_friends_tweets(username, 10, 10)
	tweets = process_user_tweets(username, 200)
	# Maps from entity name to a list of Entities with that name
	entities_map = {}
	print("Analyzing tweets...")
	print(len(tweets))
	for tweet in tweets:
		entities = google_get_entity_sentiments(tweet['text'])
		for entity in entities:
			if keyword_in_db(entity.name):
				# google_analyze_entity_sentiment(tweet['text'], entities_map)
				google_analyze_entity_sentiment(entity, entities_map)
	print("Getting top entities...")
	top_n = get_top_n(entities_map, 5)
	result = {}
	for e in top_n:
		result[e.name] = e.avg_score()
	resp = make_response(json.dumps(result))
	resp.headers['Content-Type'] = "application/json"
	return resp

@app.route("/spectrum", methods=['POST'])
def sendSpectrum():
	politicalScore = 0
	count = 0
	username = request.form['username']
	# print("Getting friends' tweets...")
	# print(username)
	# tweets = process_friends_tweets(username, 10, 10)
	tweets = process_user_tweets(username, 200)
	# print("Analyzing tweets...")
	for tweet in tweets:
		politicalScore += int(getMLClassifier(tweet['text']))
		count +=1
	resp = make_response(json.dumps(politicalScore/count))
	resp.headers['Content-Type'] = "application/json"
	return resp

if __name__ == "__main__":
	app.run(debug = True)
