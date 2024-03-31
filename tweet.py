from requests_oauthlib import OAuth1Session
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
url_text = 'https://api.twitter.com/2/tweets'


def main():
    twitter = OAuth1Session(CONSUMER_KEY, 
                            client_secret = CONSUMER_SECRET,
                            resource_owner_key=ACCESS_KEY,
                            resource_owner_secret=ACCESS_KEY_SECRET)
    #
    fetch_response = twitter.fetch_request_token(request_token_url,
                            params={"x_auth_access_type": 'write'})
    print(fetch_response)
    resource_owner_key = fetch_response.get('oauth_token')
    resource_owner_secret = fetch_response.get('oauth_token_secret')
    #
    text = CONSUMER_KEY + ":" + CONSUMER_SECRET
    token_headers={
        'Authorization': 'Basic ' + base64.b64encode(text.encode()).decode()
    }
    oauth_response = requests.post(token_url, 
                        header  = token_headers,
                        params={
                            "grant_type": "client_credentials"
                        })
    print(oauth_response)
    #
    res = twitter.post(url_text, params={"text": url_text})
    print(res)
    print(res.text)
                        
    
if __name__ == "__main__":
    main()

