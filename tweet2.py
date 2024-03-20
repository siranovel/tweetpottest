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



auth_url = 'https://api.twitter.com/i/oauth2/authorize'
access_token_url = 'https://api.twitter.com/oauth2/token'
url_text = 'https://api.twitter.com/2/tweets'
tweet = 'New commit pushed! (oauth 2.0)'

def main():
    # OAuth2Sessionの認証処理
    text =  CLIENT_ID + ":" + CLIENT_SECRET
    headers={ "Authorization": "Bearer "+base64.b64encode(text.encode()).decode(),
              'Content-Type': 'application/x-www'}
   
          
    # step 1
    basic = HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    oauth = OAuth1Session(CLIENT_ID, 
                          client_secret=CLIENT_SECRET
                            )
    # step 2
    token_response = requests.get(auth_url,
                        headers=headers,
                        params =  {
                            "respose_type": 'code',
                            "client_id": CLIENT_ID,
                            "redirect_url": 'https://twitter.com/',
                            "scope": parse.quote(" ".join(scopes))
                        } 
                              )
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
