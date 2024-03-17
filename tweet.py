from requests_oauthlib import OAuth1Session
from requests.auth     import HTTPBasicAuth
import os

CONSUMER_KEY = os.environ.get("TWITTER_CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("TWITTER_CONSUMER_SECRET")
ACCESS_KEY = os.environ.get("TWITTER_ACCESS_TOKEN")
ACCESS_KEY_SECRET = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")

request_token_url = 'https://api.twitter.com/oauth/request_token'
base_authorization_url = 'https://api.twitter.com/oauth/authorize'
access_token_url = 'https://api.twitter.com/oauth/access_token'
url_text = 'https://api.twitter.com/1.1/statuses/update.json'
tweet = 'New commit pushed!'
headers={'Content-Type': 'application/json'}
def main():
    # OAuth1Sessionの認証処理
    basic = HTTPBasicAuth(CONSUMER_KEY, CONSUMER_SECRET)
    # step 1
    twitter = OAuth1Session(CONSUMER_KEY, client_secret=CONSUMER_SECRET)
    res = twitter.post(url_text, auth=basic, params = {'status': tweet})
    print(res)

if __name__ == "__main__":
    main()
