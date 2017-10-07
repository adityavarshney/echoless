from pymongo import MongoClient, Connection
import json

client = MongoClient()
db = client['echoless']
postings = db.postings_collection

result = db.tweets.insert_many(
	"hashtags": {
	
	}
)

# hashtags
# id
# retweet_count
# retweet_user (optional)
# user_id
# text
# media (optional): 
# 	url/ type 