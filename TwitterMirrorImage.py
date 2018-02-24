import tweepy
import config

def parseTweets(userName):
	#authorizes the twitter account to be able to access tweets
	auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
	auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_SECRET)
	api = tweepy.API(auth)

	tweetsFromUser = []

	recentTweets = api.user_timeline(screen_name = userName, count = 100, tweet_mode = "extended")
	tweetsFromUser = [[tweet.full_text] for tweet in recentTweets]

	return tweetsFromUser

check = parseTweets("realDonaldTrump")
print(check)



