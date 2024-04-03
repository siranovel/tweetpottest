from requests_oauthlib import OAuth1
import os
import base64
import requests

CONSUMER_KEY = os.environ.get("TWITTER_CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("TWITTER_CONSUMER_SECRET")
ACCESS_KEY = os.environ.get("TWITTER_ACCESS_TOKEN")
ACCESS_KEY_SECRET = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")
tweet = 'New commit pushed! (twitter v2 oauth 1.0a)'

request_token_url = 'https://api.twitter.com/oauth/request_token'
token_url = 'https://api.twitter.com/oauth2/token'
access_token_url = 'https://api.twitter.com/oauth/access_token'
url_text = 'https://api.twitter.com/2/tweets'
def main():
    #
    header_ouath = OAuth1(CONSUMER_KEY, 
                       client_secret = CONSUMER_SECRET,
                       resource_owner_key=ACCESS_KEY,
                       resource_owner_secret=ACCESS_KEY_SECRET,
                       decoding=None)
    ses = requests.Session()
    res = ses.post(url_text, json={"text": tweet}, auth=header_ouath)                       
    #
    print(res)
    print(res.text)
                        
    
if __name__ == "__main__":
    main()

