from requests_oauthlib import OAuth1Session
from requests_oauthlib import OAuth1
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
scope = "tweet.write,tweet.read"
def main():
    # OAuth1Sessionの認証処理
    oauth = OAuth1Session(CONSUMER_KEY, client_secret=CONSUMER_SECRET, callback_uri='https://twitter.com/')
    fetch_response = oauth.fetch_request_token(request_token_url)
    resource_owner_key = fetch_response.get('oauth_token')
    resource_owner_secret = fetch_response.get('oauth_token_secret')
    authorization_url = oauth.authorization_url(base_authorization_url)
    print( authorization_url)
    ridirect_response = authorization_url+"&response_type=code&scope="+scope
    oauth_response =  oauth.parse_authorization_response(ridirect_response)
    print(oauth_response)
    print("aaaaaaaaaaaaaaaaaaaaa")
    res = oauth.post(url_text, params = {'status': tweet})
    print(res)

if __name__ == "__main__":
    main()
