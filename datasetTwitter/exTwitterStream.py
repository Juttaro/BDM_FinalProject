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


# APP_KEY = ""
# APP_SECRET = ""
# OAUTH_TOKEN = ""
# OAUTH_TOKEN_SECRET = ""

# # ======= Ames KEY ===========
#
# APP_KEY = "aW5ds2Mq65CSmHtesWHypgdrG"
# APP_SECRET = "qjY9G9VriIpMCaRsR1kgV6mCL3HVJlQ4FTEOnzeKByvJD9KFSi"
# OAUTH_TOKEN = "834103546601672705-MXXFPwSgz1nMoSsTeiGmC1p7WQ3ljM6"
# OAUTH_TOKEN_SECRET = "QKMTpoywTvpvT1qWP0VqvW9B8FBRp2TrOOP74Ab3JCHUW"
#
# # =============================

# ========James's KEY==========
APP_KEY = "LWnaGn2ZbLwNa9SYzwbeFz5vQ"
APP_SECRET = "ZQgTvpYzJhDRe0xoROkm2o6AqviZiHtiQIL9uFHS0wBINYN7Sw"
OAUTH_TOKEN = "850102013174177792-pfalrKryY1o5mQ9WrQRnj1EBrYIaOYf"
OAUTH_TOKEN_SECRET = "eg0Kfv0EgZ4e2aNtf6tney9lI12S4MlynXkcWIVfiVODE"
#==============================


twtToJSON = codecs.open('stream_twt.json','w', 'utf-8')

# Disconnection fails bc you can not recieve the data fast enough

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

    def on_error(self, status_code):
        print status_code

if __name__ == '__main__':
    print 'Streaming...'
    #opening json array
    twtToJSON.write('[')

    while True:
        try:
            stream = MyStreamer(APP_KEY, APP_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
            stream.statuses.filter(locations='-125,30,-65,50')
        # except IncompleteRead:
        #     print 'Incomplete'
        #     continue

        except KeyboardInterrupt:
            stream.disconnect()
            # remove the last comma of the json list
            twtToJSON.seek(-1, 2)
            #close the json list
            twtToJSON.write(']')
            # close file
            twtToJSON.close()
            print '...Stream END'
            break

        except BaseException, e:
            print 'failed on', str(e)
            print '\nsleeping'
            time.sleep(5) #Do not end while sleeping
            print '\nstreaming starting again'
