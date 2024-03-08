from requests_oauthlib import OAuth1Session
import os

CONSUMER_KEY = os.environ.get("TWITTER_CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("TWITTER_CONSUMER_SECRET")
ACCESS_KEY = os.environ.get("TWITTER_ACCESS_TOKEN")
ACCESS_KEY_SECRET = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")

request_token_url = 'https://api.twitter.com/oauth/request_token'
url_text = 'https://api.twitter.com/1.1/statuses/update'
tweet = 'New commit pushed!';

def main():
    # OAuth1Sessionの認証処理
    oauth = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET)
    fetch_response = oauth.fetch_request_token(request_token_url)
    print(fetch_response)
    print( "4444444444444444444444")
    res = oauth.post(url_text, params = {'status': tweet})
    print(fetch_response)

if __name__ == "__main__":
    main()
