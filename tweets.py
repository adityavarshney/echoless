import json
import twitter

api = twitter.Api(consumer_key='EmONxqVj70y1d6wF3SdxwXzf4',
  consumer_secret='8XismvLv6ZFlzTtQmCT8Pdzu9iQw9SshKQ0Z9mu2Fg8y4oX8rU',
  access_token_key='3574966759-PLVcrtJPVY366L1UGnPoqDTmOjfpNSAKOzGsd04',
  access_token_secret='DGloqGNZtsRC1UcTLmI7kGKGNBBH4rvRoxG65YKTLrRln')

# user's own tweets
def process_user_tweets(username, count = 10):
	user = api.GetUser(screen_name=username)
	user_id = user.id
	t = api.GetUserTimeline(user_id, count, exclude_replies=True)
	tweets = [i.AsDict() for i in t]
	return tweets

# user's friends' IDs to get their tweets
def process_friends_tweets(username, count=10, friends_count=10):
	user = api.GetUser(screen_name=username)
	user_id = user.id
	friends = api.GetFriendIDs(user_id)[:friends_count]
	all_friends_tweets = [] 
	for f in friends:
		f_t = api.GetUserTimeline(f, count=count, exclude_replies=True)
		f_tweets = [i.AsDict() for i in f_t]
		for tweet in f_tweets:
			tweet_json = tweet_to_json(tweet)
		all_friends_tweets.append(f_tweets)
	return f_tweets 

def tweet_to_json(tweet):
	tweet_info = {}
	tweet_info['hashtags'] = tweet['hashtags']
	tweet_info['id'] = tweet['id']
	if 'retweet_count' in tweet:
		tweet_info['retweet_count'] = tweet['retweet_count']
	if 'retweeted_status' in tweet:
		tweet_info['retweet_user'] = tweet['retweeted_status']['user']['id']
	tweet_info['user_id'] = tweet['user']['id'] 
	tweet_info['text'] = tweet['text']
	if 'media' in tweet:
		tweet_info['media_url'] = tweet['media'][0]['media_url_https']
		tweet_info['media_type'] = tweet['media'][0]['type']
	return json.dumps(tweet_info)

# user's own tweets
def process_user_tweets_training(username, count = 10):
	user = api.GetUser(screen_name=username)
	user_id = user.id
	t = api.GetUserTimeline(user_id, count)
	tweets = [i.AsDict() for i in t]
	return tweets
