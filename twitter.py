import requests
from requests_oauthlib import OAuth1
import json

params={'q':'#ModiInChina','result':'mixed','until':'2015-05-18'}#add your query to 'q' key
url = 'https://api.twitter.com/1.1/search/tweets.json'#using twitter search
auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET',
                  'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')# add twitter oauth details
r=requests.get(url, auth=auth,params=params)
print r.status_code
r=r.json()
tweets=r['statuses']
l=len(tweets)
print 'The Tweets for your entered query are:'
for tweet in tweets:
	print 'Tweet %d :'%(l)+tweet['text']
	l=l-1
