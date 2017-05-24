#This script uses twython to interface Twitter's Stream API
"""
Documentation:  https://twython.readthedocs.io/en/latest/
Requirements:   pip install twython
"""

import random
import json
import codecs
from httplib import IncompleteRead
from twython import TwythonStreamer
import time

APP_KEY = "TKTfiGJl2TE32Gh24gCRIdP4J"
APP_SECRET = "yLjbGEv9TjBNLKmVZOSkIwfP6kij400YkgNB4wPLCJDPAAfUCM"
OAUTH_TOKEN = "848331199504363520-UmfEjp6vNUCGVhz8CEIuG52JZpXBySf"
OAUTH_TOKEN_SECRET = "GaiFuI0ssvI7y2EwMo9J0xmazFDdEQnw9uO1hYbZ3TfLA"

twtToJSON = codecs.open('testing.jsonl', 'w', 'utf-8')
nytkeywords = []
with open('Top100People.txt') as peep, open('Top100Subjects.txt') as sub, open('Top100Organizations.txt') as org:
    peepkeywords = peep.readlines()
    nytkeywords += [x.strip('\n') for x in peepkeywords]

    subkeywords = sub.readlines()
    nytkeywords += [x.strip('\n') for x in subkeywords]

    orgkeywords = org.readlines()
    nytkeywords += [x.strip('\n') for x in orgkeywords]

    random.shuffle(nytkeywords)
    #print(nytkeywords)

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
            stream.statuses.filter(locations='-125,30,-65,50', track=nytkeywords, languages='en')

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
