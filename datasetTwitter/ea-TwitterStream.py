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
import csv

# ======= Ames KEY ===========

APP_KEY = "aW5ds2Mq65CSmHtesWHypgdrG"
APP_SECRET = "qjY9G9VriIpMCaRsR1kgV6mCL3HVJlQ4FTEOnzeKByvJD9KFSi"
OAUTH_TOKEN = "834103546601672705-MXXFPwSgz1nMoSsTeiGmC1p7WQ3ljM6"
OAUTH_TOKEN_SECRET = "QKMTpoywTvpvT1qWP0VqvW9B8FBRp2TrOOP74Ab3JCHUW"

# =============================


# Basic class that will just print the stream of tweets to stdout
class CustomStreamListener(StreamListener):

    def on_data(self, data):
        print "     FETCHING..."

        decoded = json.loads(data)  # Loads the data from stream into decoded

        # with open('ea_dbTweets.csv', 'w') as handle:
        #
        #     writer = csv.writer(handle)
        #     writer.writerow(['Screen_Name', 'Tweet'])
        #     writer.writerows((decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore')))


            #handle.write('user, username, tweet')
            #handle.writerow(data.user.screen_name, data.created_at, data.text)

            #print "\n", data.user.screen_name, data.created_at, data.text

        print (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))

        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    print "START STREAM"

    # This handles the identification
    l = CustomStreamListener()
    auth = OAuthHandler(APP_KEY, APP_SECRET )
    auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


    stream = Stream(auth, l)
    # On this line we will filter by whatever parameters we choose
    stream.filter(locations=[-74.1687, 40.5722, -73.8062, 40.9467])




