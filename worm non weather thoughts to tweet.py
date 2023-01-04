import tweepy

# API keys that I saved
api_key = "8NZVUbCDIiicD5CxpZZEENzde"
api_secret = "r04pHaAjKnSgBQwRNtzeSN4avEZKKn6Syyw0JGHvt9eqlQkJhf"
access_token = "1610122102585331712-7kTBuyQSZ1PbeE3i64BxpVQlniWQfo"
access_secret = "jM6lCYRXr2V1SOYMihLOHIbXF3ipHNxmfXGXaoCF2eKrl"

#authenticate to twitter
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

#list of tweets a worm could tweet
my_list = []
my_list = ["the soil i am traveling through right now feels so soft",
           "i really hope a chicken does not cross the sidewalk atm (i wish to not be eaten)",
           "can a worm have a little lexapro as a treat",
           "my mom says i can play if your mom tells you not to cut me in half",
           "just learned that the reason my house smells bad is because dogs poop here. messed up fr",
           "took a little bath in a puddle today",
           "god what a great day to be a worm",
           "another day of being the cutest worm",
           "my name is worm and i am the coolest squiggle",
           "someone salted the floor it hurts to move"]

#picking a random tweet from the list of worm thoughts
import random
random.choice(my_list)

#schedule the tweet
import schedule
import time
def job():

#tweet
    status = random.choice(my_list)
    api.update_status(status)

schedule.every().day.at("18:50").do(job)
while 1:
   schedule.run_pending()
   time.sleep(1)




