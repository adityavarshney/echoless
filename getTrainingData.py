#creating training data
import csv
import pandas as pd
import twitter
from tweets import process_user_tweets, api

df1 = pd.read_csv("senatorTwitterHandles.csv")

senatorTweets = {}
for senatorHandle in df1['TwitterHandles']:
	USER = api.GetUser(screen_name=senatorHandle)
	tweets = process_user_tweets(USER.id, 300) #list of 300 tweets
	senatorTweets[senatorHandle] = tweets

senatorIndex = {}
for i in range(len(df1['TwitterHandles'])):
	senatorIndex[str(df1['TwitterHandles'][i])] = i+1

# dictionary of tweetText to score

tweetScore = {}
def createIndexScores():
	for senatorHandle in senatorTweets:
		for tweet in senatorTweets[senatorHandle]:
			score = senatorIndex[senatorHandle]
			tweetScore[tweet['text']] = score

createIndexScores()

#writing to csv files
with open('allSenatorTweetsAndScores.csv', 'w') as csv_file:
	writer = csv.writer(csv_file)
	for key, value in tweetScore.items():
		writer.writerow([key, value])


