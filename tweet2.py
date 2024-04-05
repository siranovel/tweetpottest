from requests_oauthlib import OAuth1Session
import os
import requests
import base64

CLIENT_ID = os.environ.get("TWITTER_CLIENT_ID")
CLIENT_SECRET = os.environ.get("TWITTER_CLIENT_SECRET")

token_url = 'https://api.twitter.com/oauth2/token'
url_text = 'https://api.twitter.com/2/tweets'
tweet = 'New commit pushed! (oauth 2.0)'
def main():
    # OAuth1
    ses = requests.Session()
    # step 1
    text = CLIENT_ID + ":" + CLIENT_SECRET
    token_headers={
        'Authorization': 'Basic ' + base64.b64encode(text.encode()).decode()
    }
    oauth_response = ses.post(token_url, 
                        headers = token_headers,
                        params={
                            "grant_type": "client_credentials"
                        }).json()
    print(oauth_response)
    #
    twitter = OAuth1Session(CLIENT_ID, 
                       client_secret = CLIENT_SECRET
                       )
    res = twitter.post(url_text, json={"text": tweet})
    print(res)
    print(res.text)

if __name__ == "__main__":
    main()

