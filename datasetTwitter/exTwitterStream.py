#Twitter streaming Api

import json
import time
from twython import Twython
from twython import TwythonStreamer
from httplib import IncompleteRead

APP_KEY = "LWnaGn2ZbLwNa9SYzwbeFz5vQ"
APP_SECRET = "ZQgTvpYzJhDRe0xoROkm2o6AqviZiHtiQIL9uFHS0wBINYN7Sw"
count = 0

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        try:
            if 'text' in data:
            #print data['text'].encode('utf-8')
                twtToJSON = open('stream_twt.json','a')
                twtToJSON.write(json.dumps(data))
                twtToJSON.close()
                return True
        except BaseException, e:
            print 'failed on', str(e)
            time.sleep(5)

        #try:
            # if 'text' in data:
        #     temp = data
        #     print data['text'].encode('utf-8')
        #     twtToJSON = open('stream_twt.json','w')
        #     twtToJSON.write(json.dumps(temp))
        #     twtToJSON.close()
        # except BaseException, e:
        #     print 'failed'
            # print data['text'].encode('utf-8')
            # print data
            # print data


    def on_error(self, status_code, data):
        print status_code


twitter = Twython(APP_KEY, APP_SECRET)

# auth = twitter.get_authentication_tokens()
#
# OAUTH_TOKEN = auth['oauth_token']
# OAUTH_TOKEN_SECRET = auth['oauth_token_secret']
#
# print OAUTH_TOKEN,OAUTH_TOKEN_SECRET, auth['auth_url']

OAUTH_TOKEN = "850102013174177792-pfalrKryY1o5mQ9WrQRnj1EBrYIaOYf"
OAUTH_TOKEN_SECRET = "eg0Kfv0EgZ4e2aNtf6tney9lI12S4MlynXkcWIVfiVODE"

while True:
    try:
        stream = MyStreamer(APP_KEY, APP_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
        stream.statuses.filter(locations='-125,30,-65,50')
    except IncompleteRead:
        continue
    except BaseException, e:
        print 'failed on', str(e)
        time.sleep(5)
    except KeyboardInterrupt:
        stream.disconnect()
        break


# stream.statuses.filter(track='#nyc')
# stream.statuses.filter(language='english')
