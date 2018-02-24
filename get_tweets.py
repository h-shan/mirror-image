import tweepy
import config
import re

def parse_tweets(userName):
    #authorizes the twitter account to be able to access tweets
    auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
    auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_SECRET)
    api = tweepy.API(auth)

    user = api.get_user(userName)
    tweetsFromUser = []

    recentTweets = api.user_timeline(screen_name = userName, count = 200, tweet_mode = "extended")
    tweetsFromUser = [tweet.full_text for tweet in recentTweets]

    return tweetsFromUser


def filterExcess(tweets):
    filteredTweets = []
    for i in range(len(tweets)):
        tweet = tweets[i]

        #removes mentions
        while "@" in tweet:
            numMentions = tweet.count("@")
            #print(numMentions)
            for i in range(numMentions):
                mentionStart = tweet.find("@")
                mentionEnd = tweet.find(" ", mentionStart)
                #print(tweet[mentionStart:mentionEnd])
                tweet = tweet.replace(tweet[mentionStart:mentionEnd],"")\

        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', tweet)

        if len(urls) > 0:
            for i in range(len(urls)):
                #print(tweet)
                #print(urls[i])
                tweet = tweet.replace(urls[i],"")

        tweet = ''.join([i if ord(i) < 128 else ' ' for i in tweet])



        filteredTweets.append(tweet.strip())



    return filteredTweets



if __name__ == '__main__':
    tweets = parse_tweets('realDonaldTrump')
    print(filterExcess(tweets))
    fh = open('tweets.txt', 'w')
    for tweet in tweets:
        fh.write(tweet)

    fh.close()

