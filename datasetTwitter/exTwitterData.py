#This script uses twython to interface Twitter's Search API
"""
Documentation:  https://twython.readthedocs.io/en/latest/
Requirements:   pip install twython
"""
import json
from twython import Twython

APP_KEY = "TKTfiGJl2TE32Gh24gCRIdP4J"
APP_SECRET = "yLjbGEv9TjBNLKmVZOSkIwfP6kij400YkgNB4wPLCJDPAAfUCM"

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

result = twitter.search(q='trending', result_type='popular')
twtToJSON = open('trending_twt.json','w')
twtToJSON.write(json.dumps(result))
twtToJSON.close()
