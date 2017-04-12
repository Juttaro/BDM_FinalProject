"""

Twitter Stream API using Tweepy
Requirements: pip install tweepy

Twython wasnt working for me and i tried using Tweepy. But then I realise it was a problem with the
Project interpreter in Pycharm. This works, the output looks like this on the console: (Maybe useful or not)

(USERNAME, TWEET)

(u'lynne8675', 'Felicity, is that you?!?!??! https://t.co/Qe9sCPAIvm')

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

        #if 'text' in data:
        decoded = json.loads(data)

            #saving = decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore')

            # saveFile = open('tweetsDB.csv', 'a')  # We want to append to the csv file
            # saveFile.write(saving)
            # saveFile.write('\n')
            # saveFile.close()

            #print data

        print (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))

        #print decoded
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
    stream.filter(locations=[-74.1687, 40.5722, -73.8062, 40.9467])




