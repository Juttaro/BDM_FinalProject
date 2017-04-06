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
