# quick script to pull data from NYTimes Most Popular API

import json
import urllib2

# Most Popular viewed
# api-key2 = 6f8d5c8a948141bdb509b0ccfef983b4
nyt_url = "https://api.nytimes.com/svc/mostpopular/v2/mostviewed/U.S./7.json?api-key=6f8d5c8a948141bdb509b0ccfef983b4"
request1 = urllib2.urlopen(nyt_url)
MostPopularSet = request1.read()
request1.close()
MostPopularToJSON = open('pop_times.json','w')
MostPopularToJSON.write(MostPopularSet)
MostPopularToJSON.close()



# STRING COMPARISON CODE
# doc1 = "You need to make your question more concrete. If you've already read the fingerprinting papers, you already know the principles at work, so describing common approaches here would not be beneficial. If you haven't, you should also check out papers on duplicate detection and various web spam detection related papers that have come out of Stanford, Google, Yahoo, and MS in recent years."
#
# doc2 = "If you've already read the fingerprinting papers, you already know the principles at work, so describing common approaches here would not be beneficial. "
#
# import re
#
# # doc1 = "hello"
# #
# # doc2 = "Hello"
#
# regex = re.compile('')
#
#
# def jaccard_similarity(doc1, doc2):
#     doc1 = doc1.lower()
#     doc2 = doc2.lower()
#
#
#     a = set(doc1.split())
#     b = set(doc2.split())
#     similarity = float(len(a.intersection(b))*1.0/len(a.union(b))) #similarity belongs to [0,1] 1 means its exact replica.
#     return similarity
#
#
# print jaccard_similarity(doc1, doc2)
