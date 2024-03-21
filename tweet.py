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
tweet = 'New commit pushed! (oauth 1.0a)'
headers={'Content-Type': 'application/json'}
def main():
    # OAuth1
    # step 1
    text = CONSUMER_KEY + ":" + CONSUMER_SECRET
    headers={
        'Authorization': 'Basic ' + base64.b64encode(text.encode()).decode()
    }
    oauth_response = requests.post(token_url, 
                        headers = headers,
                        params={
                            "grant_type": "client_credentials"
                        })
    print(oauth_response)
    print(oauth_response.text)
    res = oauth.post(url_text, params = {'status': tweet})
    print(res)

if __name__ == "__main__":
    main()
