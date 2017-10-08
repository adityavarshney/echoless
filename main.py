from tweets import process_friends_tweets, process_user_tweets
from analyze import google_analyze_entity_sentiment, get_top_n
<<<<<<< HEAD
from flask import Flask, render_template, redirect, url_for, request, make_response

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def complete(username):
	message = None
	if request.method == 'POST':
		datafromjs = request.form['mydata']
		# google_analyze_entity_sentiment("I hate taxes they make me pay money to the government which I also hate", {})
		print("Getting friends' tweets...")
		# tweets = process_friends_tweets(username, 50, 25)
		tweets = process_user_tweets(username, 1000)
		# Maps from entity name to a list of Entities with that name
		entities_map = {}
		print("Analyzing tweets...")
		for tweet in tweets:
			google_analyze_entity_sentiment(tweet['text'], entities_map)
		print("Getting top entities...")
		top_n = get_top_n(entities_map, 20)
		for e in top_n:
			result += str(e.name) + "," + str(e.score_sum/e.count) + "\n"
			# print(e.name)
			# print(e.salience_sum)
			# print(e.count)
			# print(e.type)
			# print(e.score_sum/e.count)
			# print(e.magnitude_sum/e.count)
			# print()
		resp = make_response('{"response": '+result+'}')
		resp.headers['Content-Type'] = "application/json"
		return resp
		return render_template('index.html', message='')
	if __name__ == "__main__":
		app.run(debug = True)

# =======
# import csv

# def run(username):
# 	# google_analyze_entity_sentiment("I hate taxes they make me pay money to the government which I also hate", {})
# 	print("Getting friends' tweets...")
# 	# tweets = process_friends_tweets(username, 50, 25)
# 	tweets = process_user_tweets(username, 200)
# 	# Maps from entity name to a list of Entities with that name
# 	entities_map = {}
# 	print("Analyzing tweets...")
# 	for tweet in tweets:
# 		google_analyze_entity_sentiment(tweet['text'], entities_map)
# 	print("Getting top entities...")
# 	top_n = get_top_n(entities_map, 20)
# 	#writing to csv files
# 	# with open('testDisplay.csv', 'w') as csv_file:
# 	# 	writer = csv.writer(csv_file)
# 	# 	writer.writerow(['keyword', 'sentiment'])
# 	# 	for e in top_n:
# 	# 		writer.writerow([e.name, e.score_sum/e.count])
# 	for e in top_n:
# 		print(e.name)
# 		print(e.salience_sum)
# 		print(e.count)
# 		print(e.type)
# 		print(e.score_sum/e.count)
# 		print(e.magnitude_sum/e.count)
# 		print()

