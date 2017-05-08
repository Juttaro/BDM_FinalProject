# quick script to pull data from NYTimes

import json
import urllib2
import sys

if __name__=='__main__':
# Most Popular viewed
# api-key2 = 6f8d5c8a948141bdb509b0ccfef983b4
    nyt_url = sys.argv[1]
    file_name = sys.argv[2]
    #nyt_url = 'https://api.nytimes.com/svc/archive/v1/2017/1.json'
    #file_name = 'archivejan1.json'
    #req = urllib2.Request(url=nyt_url+'?&api-key=6f8d5c8a948141bdb509b0ccfef983b4')
    request = urllib2.urlopen(nyt_url+'?&api-key=6f8d5c8a948141bdb509b0ccfef983b4')
    status = request.read()
    request.close()
    statusToJSON = open(file_name,'w')
    statusToJSON.write(status)
    statusToJSON.close()
