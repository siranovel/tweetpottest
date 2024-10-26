tweetpottst
===========
X(旧Twitter)に、potするだげ

## Usage ##

See action.yml

## Basic ##

~~~
    steps:
      - uses: siranovel/tweetpot@v1.0.0
        with:
          text: 'New commit pushd! at tweepy'
          twitter_consumer_key: ${{ secrets.TWITTER_CONSUMER_API_KEY }}
          twitter_consumer_secret: ${{ secrets.TWITTER_CONSUMER_API_SECRET_KEY }}
          twitter_access_token: ${{ secrets.TWITTER_ACCESS_TOKEN_KEY }}
          twitter_access_token_secret: ${{ secrets.TWITTER_ACCESS_TOKEN_SECRET }}
~~~

## Optional ##

## Environment variables ##

## Inputs ##

|Name                       |Description                      |Default                 |Required|
|---------------------------|---------------------------------|------------------------|------------------------|
|text                       |X(Twitter) pot text              |${{ github.repository }}|yes     |
|twitter_consumer_key       |Twitter API consumer key         |                        |yes     |
|twitter_consumer_secret    |Twitter API consumer secret key  |                        |yes     |
|twitter_access_token       |Twitter API access token         |                        |yes     |
|twitter_access_token_secret|Twitter API consumer token secret|                        |yes     |

## Outputs ##

## Supported ##

## Dependencies ##

  * python >= 3.10

## Contributing ##

## License ##
[MIT](LICENSE)








