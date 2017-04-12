"""

Twitter Stream API using Tweepy
Requirements:   pip install tweepy

"""

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

# ======= Ames KEY ===========

APP_KEY = "aW5ds2Mq65CSmHtesWHypgdrG"
APP_SECRET = "qjY9G9VriIpMCaRsR1kgV6mCL3HVJlQ4FTEOnzeKByvJD9KFSi"
OAUTH_TOKEN = "834103546601672705-MXXFPwSgz1nMoSsTeiGmC1p7WQ3ljM6"
OAUTH_TOKEN_SECRET = "QKMTpoywTvpvT1qWP0VqvW9B8FBRp2TrOOP74Ab3JCHUW"

# =============================


# Basic class that will just print the stream of tweets to stdout
class StdOutListener(StreamListener):
    def on_data(self, data):
        #decoded = json.loads(data) 
        print data
        #print (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    print "START STREAM"

    # This handles the identification
    l = StdOutListener()
    auth = OAuthHandler(APP_KEY, APP_SECRET )
    auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    stream = Stream(auth, l)

    # On this line we will filter by whatever parameters we choose
    stream.filter(track=['trump'])



