import os
import tweepy

def main() -> None:
    tweet = os.getenv("INPUT_TEXT")
    CONSUMER_KEY = os.environ.get("INPUT_TWITTER_CONSUMER_KEY")
    CONSUMER_SECRET = os.environ.get("INPUT_TWITTER_CONSUMER_SECRET")
    ACCESS_KEY = os.environ.get("INPUT_TWITTER_ACCESS_TOKEN")
    ACCESS_KEY_SECRET = os.environ.get("INPUT_TWITTER_ACCESS_TOKEN_SECRET")

    # オブジェクト作成
    client = tweepy.Client(
        consumer_key = CONSUMER_KEY,
        consumer_secret = CONSUMER_SECRET,
        access_token = ACCESS_KEY,
        access_token_secret = ACCESS_KEY_SECRET)
    # ツィートする
    res = client.create_tweet(text=tweet)
    print(res)

if __name__ == "__main__":
    main()
