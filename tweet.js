const OAuth = require('oauth').OAuth;
const Twitter = require('twitter-lite');
const user = new Twitter({
  subdomain: "api",
  version: "1.1",
  client_id=process.env.TWITTER_CLIENT_ID,
});
user
  .get("oauth/token", {
    response_type=code,
    redirect_uri='https://twitter.com/',
    scope='tweet.write',
  })
  .then((result) => {
    console.log(result);
  })
  .catch((error) => {
    console.error(error);
  });





// const response = await user.getBearerToken();
const app = new Twitter({
  subdomain: "api",
  version: "2",
  extension: false,
  consumer_key: process.env.TWITTER_CONSUMER_KEY,
  consumer_secret: process.env.TWITTER_CONSUMER_SECRET,
  access_token_key: process.env.TWITTER_ACCESS_TOKEN,
  access_token_secret: process.env.TWITTER_CCESS_TOKEN_SECRET,
});

const tweet = 'New commit pushed to ${process.env.GITHUB_REPOSITORY}!';

app
  .post("statuses/update", {
    status: tweet,
  })
  .then((result) => {
    console.log("Tweeted successfully!");
  })
  .catch((error) => {
    console.error(error);
  });
