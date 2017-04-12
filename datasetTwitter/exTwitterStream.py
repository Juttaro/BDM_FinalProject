#This script uses twython to interface Twitter's Stream API
"""
Documentation:  https://twython.readthedocs.io/en/latest/
Requirements:   pip install twython
"""

import json
import codecs
from twython import TwythonStreamer

APP_KEY = "LWnaGn2ZbLwNa9SYzwbeFz5vQ"
APP_SECRET = "ZQgTvpYzJhDRe0xoROkm2o6AqviZiHtiQIL9uFHS0wBINYN7Sw"
OAUTH_TOKEN = "850102013174177792-pfalrKryY1o5mQ9WrQRnj1EBrYIaOYf"
OAUTH_TOKEN_SECRET = "eg0Kfv0EgZ4e2aNtf6tney9lI12S4MlynXkcWIVfiVODE"

twtToJSON = codecs.open('stream_twt.json','w', 'utf-8')

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            twtToJSON.write(json.JSONEncoder(ensure_ascii=False).encode(data)+',')

    def on_error(self, status_code, data):
        print status_code

if __name__ == '__main__':
        try:
            print 'Streaming...'
            twtToJSON.write('[')
            stream = MyStreamer(APP_KEY, APP_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
            stream.statuses.filter(locations='-125,30,-65,50')

        except KeyboardInterrupt:
            stream.disconnect()
            #remove the last comma of the json list
            twtToJSON.seek(-1, 2)

            #close the json list
            twtToJSON.write(']')
            twtToJSON.close()
            print '...Stream END'
