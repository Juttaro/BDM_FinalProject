# Twitter stream using Tweepy


from tweepy import OAuthHandler
from tweepy import StreamListener

# ======= Ames KEY ===========

APP_KEY = "rrQ5MI42qKKWkgwyYND4TRoO7"
APP_SECRET = "cLww0LwlUODcQiSihPevwGw5y7rIrs1EIb5dV62mD0hhYAm4U0"
OAUTH_TOKEN = "	834103546601672705-Zz9d6koz1OSdVjVJXzkkZB39KsKzwdp"
OAUTH_TOKEN_SECRET = "F1hG9eeG6bDGT5uvaboX4F11lft5vFrmnzspNHdzkYSVe"

# =============================

class listener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status

print "START"

auth = OAuthHandler(APP_KEY, APP_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
twitterStream = StreamListener(auth)
#twitterStream.filter(locations=['-125,30,-65,50'])

