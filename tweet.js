var Twitter = require("twitter");

var client = new Twitter({
  consumer_key: '',
  consumer_secret: '',
  access_token_key: '',
  access_token_secret: ''
});

var myargs = process.argv.slice(2);

client.post('statuses/update', {status: myargs[0]},  function(error, tweet, response) {
  if(error) throw error;
  else{ console.log("tweeted");}
});
