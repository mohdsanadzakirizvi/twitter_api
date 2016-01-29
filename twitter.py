import requests
from requests_oauthlib import OAuth1
import json
from datetime import date


def main_func(q):  # main function
    limit = int(raw_input('Enter the number of tweets you want :\t'))
    current_time = date.today()  # get the local date
    url = 'https://api.twitter.com/1.1/search/tweets.json'
    params = {'q': q, 'result': 'mixed', 'until': current_time, 'count': limit}
    auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET', 'USER_OAUTH_TOKEN',
                  'USER_OAUTH_TOKEN_SECRET')  # add your auth details here
    r = requests.get(url, auth=auth, params=params)
    status = r.status_code
    print status
    if status == 200:
        display_tweets(r)


def display_tweets(r):  # diaplay the tweets
    r = r.json()  # parse the json
    tweets = r['statuses']
    l = len(tweets)
    print 'The Tweets for your entered query are:'
    for tweet in tweets:
        print 'Tweet %d :' % (l)+tweet['text']
        l -= 1

q = raw_input('Enter the query you want tweets for :\t')
if q:
    main_func(q)
