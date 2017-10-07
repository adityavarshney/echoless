import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 \
  as Features
import twitter
import requests

username = "a540517a-242d-48a7-9efd-7d508cbe0268"
password = "Z6xSAluM2q1s"

# tweet = "A glorious day in America! President @realDonaldTrump upholds our right of religious freedom. God bless America"
# tweet = "So many men are just fucking gross. Predators and perverts. Trump and Weinstein and others."

# natural_language_understanding = NaturalLanguageUnderstandingV1(
#   username=username,
#   password=password,
#   version="2017-02-27")

# response = natural_language_understanding.analyze(
#   text=tweet,
#   features=[
#     Features.Entities(
#       emotion=True,
#       sentiment=True,
#       limit=3
#     ),
#     Features.Concepts(
#       limit=3
#     ),
#     Features.Keywords(
#       emotion=True,
#       sentiment=True,
#       limit=3
#     )
#   ]
# )

# print(json.dumps(response, indent=2))

api = twitter.Api(consumer_key='EmONxqVj70y1d6wF3SdxwXzf4',
  consumer_secret='8XismvLv6ZFlzTtQmCT8Pdzu9iQw9SshKQ0Z9mu2Fg8y4oX8rU',
  access_token_key='3574966759-PLVcrtJPVY366L1UGnPoqDTmOjfpNSAKOzGsd04',
  access_token_secret='DGloqGNZtsRC1UcTLmI7kGKGNBBH4rvRoxG65YKTLrRln')

user = api.GetUser(screen_name='A_Varshn007')
user_id = user.id

# t = api.GetUserTimeline(user_id, count=10)
# tweets = [i.AsDict() for i in t]
# for t in tweets:
#     print(t['text'])

friends = api.GetFriendIDs(user_id)
print(friends)

