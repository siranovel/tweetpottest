from requests.auth     import HTTPBasicAuth
from requests_oauthlib import OAuth2Session
import requests
import os
import hashlib
import base64
import urllib.parse as parse

CLIENT_ID = os.environ.get("TWITTER_CLIENT_ID")
CLIENT_SECRET = os.environ.get("TWITTER_CLIENT_SECRET")
REPO = os.environ.get("REPOSITORY_NAME")
redirect_uri = 'https://twitter.com/'
scopes = ["tweet.read", "tweet.write", "user.read",
          "offline.access"]
code_verifier = hashlib.sha256(os.urandom(128)).hexdigest()
code_challenge_sha256 = hashlib.sha256(code_verifier.encode()).digest()
code_challenge = base64.urlsafe_b64encode(code_challenge_sha256).decode().rstrip("=")

auth_url = 'https://api.twitter.com/i/oauth2/authorize'
token_url = 'https://api.twitter.com/2/oauth2/token'
url_text = 'https://api.twitter.com/2/tweets'
tweet = 'New commit pushed! (oauth 2.0)'
headers={'Content-Type': 'application/x-www'}
def main():
    print(REPO)
    # OAuth2Sessionの認証処理
    # step 1
    basic = HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    oauth = OAuth2Session(client_id=CLIENT_ID, 
                          token=CLIENT_SECRET
                            )
    # step 2
    token_response = oauth.get(auth_url,
                        params =  {
                            "respose_type": 'code',
                            "client_id": CLIENT_ID,
                            "redirect_url": 'https://twitter.com/',
                            "scope": parse.quote(" ".join(scopes))
                        },
                        auth=basic)
    print(token_response)
    print(token_response.text)

    res = requests.post(access_token_url, 
                        params={
                            "grant_type": "client_credentials"
                        },
                        auth=basic)
    print(res)
    print(res.text)

if __name__ == "__main__":
    main()
