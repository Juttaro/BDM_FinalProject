#This script uses twython to interface Twitter's Stream API
"""
Documentation:  https://twython.readthedocs.io/en/latest/
Requirements:   pip install twython
"""

import json
import codecs
from httplib import IncompleteRead
from twython import TwythonStreamer
import time

APP_KEY = ""
APP_SECRET = ""
OAUTH_TOKEN = ""
OAUTH_TOKEN_SECRET = ""

twtToJSON = codecs.open('stream_twt.jsonl', 'w', 'utf-8')

# Disconnection fails bc you can not recieve the data fast enough

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            if 'retweeted_status' in data or 'quoted_status' in data:
                #print("\tcontinue streaming...")
                twtToJSON.write(json.JSONEncoder(ensure_ascii=False).encode(data)+'\r\n')

    def on_error(self, status_code, data):
        print "ERROR", status_code

if __name__ == '__main__':
    print 'Streaming...'
    #opening json array
    #twtToJSON.write('[')

    while True:
        try:
            stream = MyStreamer(APP_KEY, APP_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET)

            """pulling data with keywords (track)"""
            stream.statuses.filter(locations='-125,30,-65,50', track=['trump','pokemon'], languages='en')

            """pulling data without keywords"""
            #stream.statuses.filter(locations='-125,30,-65,50', languages='en')

        except KeyboardInterrupt:
            stream.disconnect()
            # remove the last comma of the json list
            twtToJSON.seek(-1, 2)
            #close the json list
            #twtToJSON.write(']')
            # close file
            twtToJSON.close()
            print '...Stream END'
            break

        except BaseException, e:
            print 'FAILED ON: ', e
            print '\nSleeping'
            print time.sleep(5)  # Do not cut stream in this 5 second window
            print '\tStream Starting again...'
