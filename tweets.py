import json
import twitter
from analyze import analyze_tweet

TWEET_COUNT = 10

api = twitter.Api(consumer_key='EmONxqVj70y1d6wF3SdxwXzf4',
  consumer_secret='8XismvLv6ZFlzTtQmCT8Pdzu9iQw9SshKQ0Z9mu2Fg8y4oX8rU',
  access_token_key='3574966759-PLVcrtJPVY366L1UGnPoqDTmOjfpNSAKOzGsd04',
  access_token_secret='DGloqGNZtsRC1UcTLmI7kGKGNBBH4rvRoxG65YKTLrRln')

USER = api.GetUser(screen_name='A_Varshn007')
USER_ID = USER.id

# user's own tweets
def process_user_tweets(userid = USER.id, count = 10):
	t = api.GetUserTimeline(userid, count)
	tweets = [i.AsDict() for i in t]
	return tweets

# user's friends' IDs to get their tweets
def process_friends_tweets():
	friends = api.GetFriendIDs(USER_ID)[:1]
	all_friends_tweets = [] 
	for f in friends:
		f_t = api.GetUserTimeline(f, count=TWEET_COUNT)
		f_tweets = [i.AsDict() for i in f_t]
		for tweet in f_tweets:
			tweet_json = tweet_to_json(tweet)
		all_friends_tweets.append(f_tweets)
	return f_tweets 

def tweet_to_json(tweet):
	tweet_info = {}
	tweet_info['hashtags'] = tweet['hashtags']
	tweet_info['id'] = tweet['id']
	tweet_info['retweet_count'] = tweet['retweet_count']
	if 'retweeted_status' in tweet:
		tweet_info['retweet_user'] = tweet['retweeted_status']['user']['id']
	tweet_info['user_id'] = tweet['user']['id'] 
	tweet_info['text'] = tweet['text']
	if 'media' in tweet:
		tweet_info['media_url'] = tweet['media'][0]['media_url_https']
		tweet_info['media_type'] = tweet['media'][0]['type']
	return json.dumps(tweet_info)

#print(process_friends_tweets())