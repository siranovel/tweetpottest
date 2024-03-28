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

def createHeaders(consumer_key, consumer_secret, access_token, access_token_secret):
    baseparam = {
        "oauth_token": access_token,
        "oauth_consumer_key": consumer_key,
        "oauth_signature_metod": "MAC-SHA1",
        "oauth_timestamp": str(int(time.time())),
        "oauth_nonce": str(random.getrandbits(64)),
        "oauth_version": "1.0"
    }
    signature = dict(baseparam)

def main():
    # OAuth1
    # step 1
    req_response = requests.post(request_token_url, 
                     params={
                         "oauth_callback": "oob",
                         "x_auth_access_type": "write"
                     })
    print(req_response)
    print(req_response.text)
    # step 2
    text = CONSUMER_KEY + ":" + CONSUMER_SECRET
    token_headers={
        'Authorization': 'Basic ' + base64.b64encode(text.encode()).decode()
    }
    token_response = requests.post(token_url, 
                        headers = token_headers,
                        params={
                            "grant_type": "client_credentials"
                        }).json()
    print(token_response['access_token'])
    tweet_headers={
        'Authorization': 'Bearer ' + token_response['access_token']
    }
    res = requests.post(url_text, 
                        headers = tweet_headers,
                        params = {'text': tweet})
    print(res)
    print(res.text)

if __name__ == "__main__":
    main()
