# get timeline tweet, return up to 3,200 of a user's most recent Tweets.
from TwitterAPI import TwitterAPI, TwitterPager
import pandas as pd
# set twitter api Authorization keys, remember the order for the keys
# api = TwitterAPI("consumer_API_key","consumer_API_secret", "access_token","access_token_secret")

api = TwitterAPI("G9c9PkikFEffLezvmhdkHpWma",
                 "2hLfuvejl3fhBp6Zxr1NMBT0jZk3LpNLdjTTKbDzWYBbZ3duRC",
                 "1250078614445608967-vOiELbylTZ0GxGrnhBouPPbLTTzCDG",
                 "GVDza7InbhVUZeme8g0Okoqsyo4WByTvZkFlZ4iX0jgJP")

def get_all_tweets(screen_name):
    pager = TwitterPager(api, 'statuses/user_timeline', {'screen_name': screen_name, 'count': 200})
    alltweets = pager.get_iterator(wait=3.5)
    outtweets = [
        [screen_name, tweet['id_str'], pd.to_datetime(tweet['created_at']), tweet['user']['location'],
         tweet['retweet_count'], tweet['favorite_count'], tweet['lang'], tweet['text']] for tweet in alltweets]

    df = pd.DataFrame(outtweets, columns=['user_name', 'id', 'create_time',  'geo', 'retweets','favorite_count',
                                          'language', 'text'])
    df.to_csv('results.csv', index=False)
    print('finish')

if __name__ == '__main__':
    get_all_tweets('google')
    
