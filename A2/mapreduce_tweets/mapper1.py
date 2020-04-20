#!/usr/bin/env python3
"""mapper1.py"""
import json
import re
import sys
han ='han'
hon = 'hon'
den = 'den'
det = 'det'
denna = 'denna'
denne = 'denne'
hen ='hen'
uni_tweets = 'uni_tweets'
count = 0
#with open('files/tweets_12.txt','r') as f:
for line in sys.stdin:
    if line!='\n':
        tweet = json.loads(line)

   
        if 'retweeted_status' in tweet:
            print('retweet',1)
            #continue
        else:
            print(uni_tweets,1)
            if re.search(han,tweet['text'],re.IGNORECASE):
                print(han,1)
            if re.search(hon,tweet['text'],re.IGNORECASE):
                print(hon,1)
            if re.search(den,tweet['text'],re.IGNORECASE):
                print(den,1)
            if re.search(det,tweet['text'],re.IGNORECASE):
                print(det,1)
            if re.search(denna,tweet['text'],re.IGNORECASE):
                print(denna,1)
            if re.search(denne,tweet['text'],re.IGNORECASE):
                print(denne,1)
            if re.search(hen,tweet['text'],re.IGNORECASE):
                print(hen,1)

    #if count>100000:
    #   break
