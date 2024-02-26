const Twitter = require('twitter-lite');
const user = new Twitter({
  subdomain: "api",
  version: "2",
  extension: false,
  consumer_key: process.env.TWITTER_CONSUMER_KEY,
  consumer_secret: process.env.TWITTER_CONSUMER_SECRET,
});
user
  .post("oauth/request_token")
  .then((result) => {
    console.log(result);
  })
  .catch((error) => {
    console.error(error);
  });



// const response = await user.getBearerToken();
const client = new Twitter({
  subdomain: "api",
  version: "2",
  extension: false,
  consumer_key: process.env.TWITTER_CONSUMER_KEY,
  consumer_secret: process.env.TWITTER_CONSUMER_SECRET,
  access_token_key: process.env.TWITTER_ACCESS_TOKEN,
  access_token_secret: process.env.TWITTER_CCESS_TOKEN_SECRET,
});

const tweet = 'New commit pushed to ${process.env.GITHUB_REPOSITORY}!';

client
  .post("statuses/update", {
    status: tweet,
  })
  .then((result) => {
    console.log("Tweeted successfully!");
  })
  .catch((error) => {
    console.error(error);
  });
