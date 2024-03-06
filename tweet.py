from requests_oauthlib import OAuth1Session
import os

CONSUMER_KEY = os.environ.get("TWITTER_CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("TWITTER_CONSUMER_SECRET")
ACCESS_KEY = os.environ.get("TWITTER_ACCESS_TOKEN")
ACCESS_KEY_SECRET = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")

url_text = 'https://api.twitter.com/2/statuses/update'

def main():
    # OAuth1Sessionの認証処理
    twitter = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_KEY_SECRET)
    res = twitter.post(url_text, params = {'status': 'New commit pushed'})
    print(res)

if __name__ == "__main__":
    main()
