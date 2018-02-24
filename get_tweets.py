import tweepy
import config

def parse_tweets(userName):
    #authorizes the twitter account to be able to access tweets
    auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
    auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_SECRET)
    api = tweepy.API(auth)

    tweetsFromUser = []

    recentTweets = api.user_timeline(screen_name = userName, count = 100, tweet_mode = "extended")
    tweetsFromUser = [tweet.full_text for tweet in recentTweets]

    return tweetsFromUser

if __name__ == '__main__':
    tweets = parse_tweets('realDonaldTrump')
    fh = open('tweets.txt', 'w')
    for tweet in tweets:
        fh.write(tweet)
    fh.close()

