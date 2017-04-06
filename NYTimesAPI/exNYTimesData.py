# quick script to test NYTimes TimesTags and Most Popular API
# prints timestags to console
# writes Most Viewed articles of the day for U.S. section to MostPop.json
# writes Most Shared articles of the day for all-sections to MostSharedviaTwitter.json
#

import json
import urllib2

# def query(term,filter,max):
#     # url = "http://api.nytimes.com/svc/suggest/v1/timestags?"
#     # api-key = "6f8d5c8a948141bdb509b0ccfef983b4"
#     # url += "api-key="+ api-key



print '\n',"Times Tag API",'\n'
url = "http://api.nytimes.com/svc/suggest/v1/timestags?query=france&api-key=6f8d5c8a948141bdb509b0ccfef983b4"
request = urllib2.urlopen(url)
TimesTagSet = request.read()
request.close()
print TimesTagSet

print '\n',"Most Popular API",'\n'
print "Most Popular API",'\n'


# Most Popular
# api-key2 = 6f8d5c8a948141bdb509b0ccfef983b4
url2 = "https://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/30.json?api-key=6f8d5c8a948141bdb509b0ccfef983b4"
request2 = urllib2.urlopen(url2)
MostPopularSet = request2.read()
request2.close()
MostPopularToJSON = open('MostPop.json','w')
MostPopularToJSON.write(MostPopularSet)
MostPopularToJSON.close()

# Most Shared Via Twitter
url3 = "http://api.nytimes.com/svc/mostpopular/v2/mostshared/all-sections/twitter/1.json?api-key=6f8d5c8a948141bdb509b0ccfef983b4"
request3 = urllib2.urlopen(url3)
MostSharedSet = request3.read()
request3.close()
MostSharedToJSON = open('MostSharedviaTwitter.json','w')
MostSharedToJSON.write(MostSharedSet)
MostSharedToJSON.close()

# print MostPopularSet
