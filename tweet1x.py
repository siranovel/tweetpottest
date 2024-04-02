from requests.auth     import HTTPBasicAuth
from requests_oauthlib import OAuth1Session
import requests
import os
import base64

CONSUMER_KEY = os.environ.get("TWITTER_CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("TWITTER_CONSUMER_SECRET")
ACCESS_KEY = os.environ.get("TWITTER_ACCESS_TOKEN")
ACCESS_KEY_SECRET = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")

request_token_url = 'https://api.twitter.com/oauth/request_token'
base_authorization_url = 'https://api.twitter.com/oauth/authorize'
token_url = 'https://api.twitter.com/oauth2/token'
url_text = 'https://api.twitter.com/2/tweets'
tweet = 'New commit pushed! (twitter v2 oauth 1.0a)'
def main():
    # OAuth1
    ses = requests.Session()
    # step 1
    text = CONSUMER_KEY + ":" + CONSUMER_SECRET
    token_headers={
        'Authorization': 'Basic ' + base64.b64encode(text.encode()).decode()
    }
    oauth_response = ses.post(token_url, 
                        headers = token_headers,
                        params={
                            "grant_type": "client_credentials"
                        }).json()
    print(oauth_response)
    print(oauth_response['access_token'])
    tweet_headers={
        'Authorization': 'Bearer ' + oauth_response['access_token']
    }
    res = ses.post(url_text, 
                        headers = tweet_headers,
                        params = {'text': tweet})
    print(res)
    print(res.text)

if __name__ == "__main__":
    main()
