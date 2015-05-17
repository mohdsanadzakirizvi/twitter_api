import requests
from requests_oauthlib import OAuth1
import json

params={'q':'#ModiInChina','result':'mixed','until':'2015-05-18'}
url = 'https://api.twitter.com/1.1/search/tweets.json'
auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET',
                  'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
r=requests.get(url, auth=auth,params=params)
print r.status_code
r=r.json()
tweets=r['statuses']
l=len(tweets)
print 'The Tweets for your entered query are:'
for tweet in tweets:
	print 'Tweet %d :'%(l)+tweet['text']
	l=l-1
