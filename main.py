from tweets import process_friends_tweets, process_user_tweets
from analyze import google_analyze_entity_sentiment, get_top_n

def run(username):
	tweets = process_friends_tweets(username)
	# Maps from entity name to a list of Entities with that name
	# Each Entity contains its type, count, sentiment score sum, sentiment magnitude sum, and salience sum
	entities_map = {}
	for tweet in tweets:
		google_analyze_entity_sentiment(tweet, entities_map)
	top_n = get_top_n(entities_map)
	print(top_n)

run('A_Varshn007')