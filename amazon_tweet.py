import requests
import pymysql
import json
import time
from datetime import datetime
import sys

conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           passwd='4320241oK@',
                           database ='twitter_500',
                           charset='UTF8MB4')
cursor = conn.cursor()

endpoint = "https://api.twitter.com/1.1/tweets/search/fullarchive/developing.json"
# #  endpoint = "https://api.twitter.com/1.1/tweets/search/30day/sandbox.json"
# #
headers = {"Authorization":"Bearer AAAAAAAAAAAAAAAAAAAAAJh5DQEAAAAAjCz8jvR3LIv8gF%2F2cVdsclN72SU%3DIz4LVXcM8V22zWNPZEX0ZMvONWX59P9UtweTUbXZSt5XqysrYx", "Content-Type": "application/json"}

# full_archive
# data = '{"query":"(#covid_19 OR #Covid19 OR #Covid OR #Coronavirus OR #Coronavirus19) lang:en", "fromDate": "202003010000", "toDate": "202003310000", "maxResults": 500}'

def get_all_tweets(company):
    token_count = 0
    data = '{"query":"from: ' + company + ' -is:retweet -is:reply lang:en ", "maxResults": 500, "fromDate": "201001010000", "toDate": "202003310000"}'
    print(data)
    response = requests.post(endpoint, data=data, headers=headers).json()
    # save amazon api results
    tmpresponse = '' + company + '_response.json'
    with open(tmpresponse, 'a') as outfile:
        json.dump(response, outfile)
    print(response)

    items = response['results']
    def inputdict4sql(item,item_name):
        try:
            tmpitem = item[item_name]
        except:
            tmpitem = 'null'
        return tmpitem

    for item in items:
        try:
            screen_name = inputdict4sql(item['user'], 'screen_name')
            created_at = datetime.strptime(inputdict4sql(item,'created_at'),'%a %b %d %H:%M:%S +0000 %Y')
            tweet_id = inputdict4sql(item,'id')
            text = inputdict4sql(item,'text')
            quote_count = inputdict4sql(item, 'quote_count')
            reply_count = inputdict4sql(item, 'reply_count')
            retweet_count = inputdict4sql(item,'retweet_count')
            favorite_count = inputdict4sql(item,'favorite_count')
            truncated = inputdict4sql(item,'truncated')
            language = inputdict4sql(item,'lang')
            try:
                extended_tweet = inputdict4sql(item['extended_tweet'],'full_text')
            except:
                extended_tweet = text
                # continue
            t=[screen_name,created_at,tweet_id,text,extended_tweet,quote_count,reply_count,retweet_count,favorite_count,truncated,language]
            sql = "insert into company_100 (screen_name,created_at,tweet_id,text,extended_tweet,quote_count,reply_count,retweet_count,favorite_count,truncated,language) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, t)
            conn.commit()
        except:
            print("Unexpected error:", sys.exc_info()[0])
            print(item)
            tmpitems = '' + company + '_item.json'
            with open(tmpitems, 'a') as outfile:
                json.dump(item, outfile)
            # continue
    next_token = response['next']
    print(next_token)
    token_count = token_count+1
    s=[company,next_token,token_count]
    sql = "insert into token (company,next_token,token_count) values (%s,%s,%s)"
    cursor.execute(sql, s)
    print('ready to commit')
    conn.commit()
    print('commited')


    for t in range(1):
        for i in range(1):
            print(i)
            data = '{"query":"from: ' + company + ' -is:retweet -is:reply lang:en ", "maxResults": 500, "fromDate": "201001010000", "toDate": "202003310000", "next":"' + next_token + '"}'
            response = requests.post(endpoint, data=data, headers=headers).json()
            print(response)
            tmpresponse = '' + company + '_response.json'
            with open(tmpresponse, 'a') as outfile:
                json.dump(response, outfile)
            next_token = response['next']
            token_count= token_count+1
            s = [company, next_token,token_count]
            sql = "insert into token (company,next_token,token_count) values (%s,%s,%s)"
            cursor.execute(sql, s)
            conn.commit()
            items = response['results']
            for item in items:
                try:
                    screen_name = inputdict4sql(item['user'], 'screen_name')
                    created_at = datetime.strptime(inputdict4sql(item, 'created_at'), '%a %b %d %H:%M:%S +0000 %Y')
                    tweet_id = inputdict4sql(item, 'id')
                    text = inputdict4sql(item, 'text')
                    extended_tweet = inputdict4sql(item['extended_tweet'],'full_text')
                    quote_count = inputdict4sql(item, 'quote_count')
                    reply_count = inputdict4sql(item, 'reply_count')
                    retweet_count = inputdict4sql(item, 'retweet_count')
                    favorite_count = inputdict4sql(item, 'favorite_count')
                    truncated = inputdict4sql(item, 'truncated')
                    language = inputdict4sql(item, 'lang')
                    t = [screen_name, created_at, tweet_id, text, extended_tweet, quote_count, reply_count, retweet_count,
                         favorite_count, truncated, language]
                    sql = "insert into company_100 (screen_name,created_at,tweet_id,text,extended_tweet,quote_count,reply_count,retweet_count,favorite_count,truncated,language) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    cursor.execute(sql, t)
                    conn.commit()
                except:
                    print(item)
                    tmpitems = '' + company + '_item.json'
                    with open(tmpitems, 'a') as outfile:
                        json.dump(item, outfile)
                    continue
        time.sleep(120)

if __name__ == '__main__':
    companies = ['Chevron']
                 # 'Merck', 'WellsFargo', 'pfizer', 'CocaCola', 'comcast', 'Boeing', 'Cisco',
                 # 'pepsi',
                 # 'Walmart', 'Citi', 'Medtronic', 'AbbottGlobal', 'McDonalds', 'Adobe', 'salesforce', 'Amgen', 'netflix',
                 # 'bmsnews', 'Costco', 'InsidePMI', 'nvidia', 'Accenture', 'thermofisher', 'honeywell', 'PayPal',
                 # 'Broadcom',
                 # 'UnionPacific', 'Oracle', 'Nike', 'IBM', 'nexteraenergy', 'TXInstruments', 'Lindeplc', 'LillyPad',
                 # 'Starbucks', 'CVSHealth', 'LockheedMartin', '3M', 'Qualcomm', 'DanaherCareers', 'generalelectric',
                 # 'AltriaNews', 'Lowes', 'usbank', 'FISGlobal', 'GileadSciences', 'BookingHoldings', 'AmericanExpress',
                 # 'UPS',
                 # 'CaterpillarInc', 'MDLZ', 'GetSpectrum', 'Cigna', 'ADP', 'CMEGroup', 'BBT', 'TJXCareers', 'AnthemInc',
                 # 'GoldmanSachs', 'Chubb', 'BDandCo', 'conocophillips', 'PNCBank', 'SPGlobal', 'Intuit', 'IntuitiveSurg',
                 # 'DominionEnergy', 'DukeEnergy', 'Fiserv', 'Target', 'Stryker_Jobs', 'SouthernCompany', 'MorganStanley',
                 # 'bostonsci', 'Allergan', 'Raytheon', 'Zoetis', 'CP_News', 'blackrock', 'Prologis', 'CharlesSchwab']
    for company in companies:
            try:
                get_all_tweets(company)
            except:
                print(company)
                with open('company_except', 'a') as outfile:
                    json.dump(company, outfile)
                continue
