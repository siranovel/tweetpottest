const Twitter = require('twitter-lite');

const user = new Twitter({
  consumer_key: process.env.TWITTER_CONSUMER_KEY,
  consumer_secret: process.env.TWITTER_CONSUMER_SECRET,
});
// const response = getBearerToken();
const client = new Twitter({
  subdomain: "api",
  version: "1.1",
  extension: false,
  bearer_token: process.env.TWITTER_BEARER_TOKEN,
  consumer_key: process.env.TWITTER_CONSUMER_KEY,
  consumer_secret: process.env.TWITTER_CONSUMER_SECRET,
  access_token_key: process.env.TWITTER_ACCESS_TOKEN,
  access_token_secret: process.env.TWITTER_CCESS_TOKEN_SECRET,
});

const tweet = 'New commit pushed to ${process.env.GITHUB_REPOSITORY}!';

client
  .post("tweets", {
    text: tweet,
  })
  .then((result) => {
    console.log("Tweeted successfully!");
  })
  .catch((error) => {
    console.error(error);
  });
