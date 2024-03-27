from requests.auth     import HTTPBasicAuth
from requests_oauthlib import OAuth1Session
import requests
import os
import hashlib
import base64
import urllib.parse as parse

CLIENT_ID = os.environ.get("TWITTER_CLIENT_ID")
CLIENT_SECRET = os.environ.get("TWITTER_CLIENT_SECRET")
redirect_uri = 'https://twitter.com/'
scopes = ["tweet.read", "tweet.write", "user.read",
          "offline.access"]
code_verifier = hashlib.sha256(os.urandom(128)).hexdigest()
code_challenge_sha256 = hashlib.sha256(code_verifier.encode()).digest()
code_challenge = base64.urlsafe_b64encode(code_challenge_sha256).decode().rstrip("=")

request_token_url = 'https://api.twitter.com/oauth/request_token'
auth_url = 'https://api.twitter.com/i/oauth2/authorize'
token_url = 'https://api.twitter.com/2/oauth2/token'
url_text = 'https://api.twitter.com/2/tweets'
tweet = 'New commit pushed! (oauth 2.0)'
headers={'Content-Type': 'application/x-www'}
def main():
    # OAuth2Sessionの認証処理
    ses = requests.Session()
    # step 1
    token_headers = {
        "oauth_callback": "oob",
        "oauth_consumer_key": CLIENT_ID,
        "oauth_consumer_secret": CLIENT_SECRET,
        "oauth_version": "2.0"}
    req_response = ses.post(request_token_url,
                        headers = ",".join(token_headers)
                        )
    print(req_response)
    print(req_response.text)
    # step 2

if __name__ == "__main__":
    main()
