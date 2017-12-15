import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import csv

CONSUMER_KEY = <<Enter_Your_Consumer_Key>>
CONSUMER_SECRET = <<Enter_Your_Consumer_Secret>>
ACCESS_KEY = <<Enter_Your_Access_Key>>
ACCESS_SECRET = <<Enter_Your_Access_Secret>>

auth = OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
api = tweepy.API(auth)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

myfile1 = open(<<Path_To/File_Name.txt>>, 'r').readlines()

class TweetListener(StreamListener):
    # A listener handles tweets are the received from the stream.
    #This is a basic listener that just prints received tweets to standard output

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status
#search
api = tweepy.API(auth)
twitterStream = Stream(auth,TweetListener())
test = api.lookup_users(user_ids=myfile1)

with open(<<Path_To/File_Name.csv>>,'a') as myfile:
    writer = csv.writer(myfile, dialect='excel')
    for user in test:
        result = user.id, user.followers_count
        writer.writerow(result)
