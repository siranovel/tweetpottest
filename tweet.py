from requests.auth     import HTTPBasicAuth
from requests_oauthlib import OAuth1Session
import os

CONSUMER_KEY = os.environ.get("TWITTER_CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("TWITTER_CONSUMER_SECRET")
ACCESS_KEY = os.environ.get("TWITTER_ACCESS_TOKEN")
ACCESS_KEY_SECRET = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")

request_token_url = 'https://api.twitter.com/oauth/request_token'
base_authorization_url = 'https://api.twitter.com/oauth/authorize'
access_token_url = 'https://api.twitter.com/oauth2/token'
url_text = 'https://api.twitter.com/1.1/statuses/update.json'
tweet = 'New commit pushed! (oauth 1.0a)'
headers={'Content-Type': 'application/json'}
def main():
    # OAuth1
    basic = HTTPBasicAuth(CONSUMER_KEY, CONSUMER_SECRET)
    oauth = OAuth1Session(CONSUMER_KEY, 
                          client_secret=CONSUMER_SECRET
                            )
    # step 1
    oauth_response = oauth.fetch_access_token(access_token_url,  verifier=False, auth=basic)
    print(oauth_response)
    res = oauth.post(url_text, params = {'status': tweet})
    print(res)

if __name__ == "__main__":
    main()
