import tweepy
import schedule
import time
import tkinter
consumer_key =
consumer_secret =
access_token =
access_token_secret =
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print(user.name)


def tweetFinan():
    api.update_status("Financial starts in the lounge in 10 minutes!")


def tweetEvals():
    api.update_status("Evals starts in the lounge in 10 minutes!")


def tweetPR():
    api.update_status("PR starts in the lounge in 10 minutes!")


def tweetIMPS():
    api.update_status("Imps starts in the lounge in 10 minutes!")


def tweetRD():
    api.update_status("R&D starts in the lounge in 10 minutes!")


def tweetHis():
    api.update_status("History starts in the lounge in 10 minutes!")


def tweetOC():
    api.update_status("OpComm starts in the lounge in 10 minutes!")


def tweetSoc():
    api.update_status("Social starts in the lounge in 10 minutes!")


def tweetEB():
    api.update_status("EBoard starts in the lounge in 10 minutes!")


schedule.every().monday.at("18:50").do(tweetPR)
schedule.every().monday.at("19:50").do(tweetFinan)
schedule.every().monday.at("20:20").do(tweetEvals)
schedule.every().tuesday.at("19:20").do(tweetIMPS)
schedule.every().tuesday.at("19:50").do(tweetRD)
schedule.every().wednesday.at("19:50").do(tweetHis)
schedule.every().wednesday.at("20:50").do(tweetOC)
schedule.every().thursday.at("19:50").do(tweetSoc)
schedule.every().thursday.at("20:20").do(tweetEB)

while True:
    schedule.run_pending()
    time.sleep(1)
