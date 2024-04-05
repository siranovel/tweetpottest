from requests_oauthlib import OAuth1Session
import os

CLIENT_ID = os.environ.get("TWITTER_CLIENT_ID")
CLIENT_SECRET = os.environ.get("TWITTER_CLIENT_SECRET")

url_text = 'https://api.twitter.com/2/tweets'
tweet = 'New commit pushed! (oauth 2.0)'
def main():
    #
    twitter = OAuth1Session(CLIENT_ID, 
                       client_secret = CLIENT_SECRET
                       )
    res = twitter.post(url_text, json={"text": tweet})
    print(res)

if __name__ == "__main__":
    main()
