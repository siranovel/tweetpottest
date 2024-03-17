from requests_oauthlib import OAuth2Session
from requests.auth     import HTTPBasicAuth
import os
import base64

CLIENT_ID = os.environ.get("TWITTER_CLIENT_ID")
CLIENT_SECRET = os.environ.get("TWITTER_CLIENT_SECRET")

base_authorization_url = 'https://api.twitter.com/i/oauth2/authorize'
access_token_url = 'https://api.twitter.com/oauth2/token'
url_text = 'https://api.twitter.com/1.1/statuses/update.json'
tweet = 'New commit pushed!'
headers={'Content-Type': 'application/json'}
def main():
    # OAuth2Sessionの認証処理
    text = CLIENT_ID + ':' + CLIENT_SECRET
    print(text)
    client_id64 = base64.b64encode(text.encode())
    print(client_id64)
    basic = HTTPBasicAuth(CONSUMER_KEY, CONSUMER_SECRET)
    # step 1
    scope = 'tweet.read tweet.write offline.access'
    # step 2
    oauth = OAuth2Session(CONSUMER_KEY, CONSUMER_SECRET)
    authorization_url = oauth.authorization_url(
        base_authorization_url, 
        response_type='code',
        client_id = CLIENT_ID,
        redirect_url = 'https://twitter.com/',
        scope= scope,
        state='state',
        code_challenge='challenge',
        code_challenge_method='plain')
    ridirect_response = oauth.parse_authorization_response(authorization_url)
    print(ridirect_response)
    fetch_response = oauth.fetch_request_token(base_authorization_url, params=ridirect_response)
    print(fetch_response)
    # step 3

if __name__ == "__main__":
    main()
