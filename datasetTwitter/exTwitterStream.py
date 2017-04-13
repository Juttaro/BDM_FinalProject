#This script uses twython to interface Twitter's Stream API
"""
Documentation:  https://twython.readthedocs.io/en/latest/
Requirements:   pip install twython
"""

import json
import codecs
from httplib import IncompleteRead
from twython import TwythonStreamer

APP_KEY = "TKTfiGJl2TE32Gh24gCRIdP4J"
APP_SECRET = "yLjbGEv9TjBNLKmVZOSkIwfP6kij400YkgNB4wPLCJDPAAfUCM"
OAUTH_TOKEN = "848331199504363520-UmfEjp6vNUCGVhz8CEIuG52JZpXBySf"
OAUTH_TOKEN_SECRET = "GaiFuI0ssvI7y2EwMo9J0xmazFDdEQnw9uO1hYbZ3TfLA"

twtToJSON = codecs.open('stream_twt.json','w', 'utf-8')

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            #twtToJSON.write(json.JSONEncoder(ensure_ascii=False).encode(data)+',')
            twtToJSON.write(json.JSONEncoder(ensure_ascii=False).encode(
                dict(
                    text=data['text'],
                    is_quote_status=data['is_quote_status'],
                    favorite_count=data['favorite_count'],
                    retweeted=data['retweeted'],
                    timestamp_ms=data['timestamp_ms'],
                    entities=data['entities'],
                    id_str=data['id_str'],
                    retweet_count=data['retweet_count'],
                    favorited=data['favorited'],
                    lang=data['lang'],
                    created_at=data['created_at'],
                    place=data['place']
                )
            )+',')

    def on_error(self, status_code, data):
        print status_code

if __name__ == '__main__':
    print 'Streaming...'
    #opening json array
    twtToJSON.write('[')

    while True:
        try:
            stream = MyStreamer(APP_KEY, APP_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
            stream.statuses.filter(locations='-125,30,-65,50')

        except IncompleteRead:
            print 'IncompleteRead'
            continue

        except KeyboardInterrupt:
            stream.disconnect()
            print '...Stream END'
            break

    #remove the last comma of the json list
    twtToJSON.seek(-1, 2)

    #close the json list
    twtToJSON.write(']')
    #close file
    twtToJSON.close()
