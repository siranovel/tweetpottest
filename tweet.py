from requests_oauthlib import OAuth1
import requests
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
    # OAuth1
    basic = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
                   resource_owner_key=ACCESS_KEY,
                   resource_owner_secret=ACCESS_KEY_SECRET)
    # step 1
    res = requests.post(url_text, params = {'status': tweet}, auth=basic)
    print(res)

if __name__ == "__main__":
    main()
