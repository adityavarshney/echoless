from tweets import process_friends_tweets, process_user_tweets
from analyze import google_analyze_entity_sentiment, get_top_n

def run(username):
	# google_analyze_entity_sentiment("I hate taxes they make me pay money to the government which I also hate", {})
	print("Getting friends' tweets...")
	tweets = process_friends_tweets(username, 5, 5)
	# Maps from entity name to a list of Entities with that name
	entities_map = {}
	print("Analyzing tweets...")
	for tweet in tweets:
		google_analyze_entity_sentiment(tweet['text'], entities_map)
	print("Getting top entities...")
	top_n = get_top_n(entities_map, 10)
	for e in top_n:
		print(e.name)
		print(e.salience_sum)
		print(e.type)
		print(e.score_sum)
		print(e.magnitude_sum)
		print()

run('A_Varshn007')