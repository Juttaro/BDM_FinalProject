#This script uses twython to interface Twitter's Stream API
"""
Documentation:  https://twython.readthedocs.io/en/latest/
Requirements:   pip install twython
"""

import json
import codecs
from twython import TwythonStreamer
from httplib import IncompleteRead

# APP_KEY = "LWnaGn2ZbLwNa9SYzwbeFz5vQ"
# APP_SECRET = "ZQgTvpYzJhDRe0xoROkm2o6AqviZiHtiQIL9uFHS0wBINYN7Sw"
# OAUTH_TOKEN = "850102013174177792-pfalrKryY1o5mQ9WrQRnj1EBrYIaOYf"
# OAUTH_TOKEN_SECRET = "eg0Kfv0EgZ4e2aNtf6tney9lI12S4MlynXkcWIVfiVODE"


# ======= Ames KEY ===========

APP_KEY = "rrQ5MI42qKKWkgwyYND4TRoO7"
APP_SECRET = "cLww0LwlUODcQiSihPevwGw5y7rIrs1EIb5dV62mD0hhYAm4U0"
OAUTH_TOKEN = "	834103546601672705-Zz9d6koz1OSdVjVJXzkkZB39KsKzwdp"
OAUTH_TOKEN_SECRET = "F1hG9eeG6bDGT5uvaboX4F11lft5vFrmnzspNHdzkYSVe"

# =============================


twtToJSON = codecs.open('stream_twt.json','a', 'utf-8')

# Disconnection fails bc you can not recieve the data fast enough

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            json.dump(data, twtToJSON, ensure_ascii=False)

    def on_error(self, status_code):
        print status_code

if __name__ == '__main__':
        try:
            print 'Streaming...'
            stream = MyStreamer(APP_KEY, APP_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
            stream.statuses.filter(locations='-125,30,-65,50')

        except KeyboardInterrupt:
            print '...Stream END'
            stream.disconnect()
            twtToJSON.close()
