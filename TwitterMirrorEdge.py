import tweepy

def parseTweets(userName):

	CONSUMER_KEY = 'SALYJG3o3YtK1zQvBadKTRQqf'
	CONSUMER_SECRET = 'fxAi3hfJtKWwuzkLNhp07CTWmo3d4iAwcWc4uSdtC9VwJtSXvK'
	ACCESS_TOKEN = '842097932-85kJcDamVo8CLCAuGJ1yr3bdo5O9GZ5Nmh7rCypQ'
	ACCESS_SECRET = 'BGrnvIoos3imGaIZM8tnHGHSrxHGADXKZnarX8bG7P7a2'

	#authorizes the twitter account to be able to access tweets
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
	api = tweepy.API(auth)

	tweetsFromUser = []

	recentTweets = api.user_timeline(screen_name = userName, count = 100, tweet_mode = "extended")
	tweetsFromUser = [[tweet.full_text] for tweet in recentTweets]

	return tweetsFromUser

check = parseTweets("realDonaldTrump")
print(check)



