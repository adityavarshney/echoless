import json
import twitter
from analyze import analyze_tweet

api = twitter.Api(consumer_key='EmONxqVj70y1d6wF3SdxwXzf4',
  consumer_secret='8XismvLv6ZFlzTtQmCT8Pdzu9iQw9SshKQ0Z9mu2Fg8y4oX8rU',
  access_token_key='3574966759-PLVcrtJPVY366L1UGnPoqDTmOjfpNSAKOzGsd04',
  access_token_secret='DGloqGNZtsRC1UcTLmI7kGKGNBBH4rvRoxG65YKTLrRln')

user = api.GetUser(screen_name='A_Varshn007')
user_id = user.id

# user's own tweets
t = api.GetUserTimeline(user_id, count=10)
tweets = [i.AsDict() for i in t]

# user's friends' IDs to get their tweets
friends = api.GetFriendIDs(user_id)
for f in friends:
	f_t = api.GetUserTimeline(f, count=10)
	f_tweets = [i.AsDict() for i in f_t]
	for tweet in f_tweets:
		analyze_tweet(tweet['text'])
