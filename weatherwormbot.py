import tweepy, time, datetime, sys, os, urllib, json

# API keys that I saved
api_key = " "
api_secret = " "
access_token = " "
access_secret = " "

#authenticate to twitter
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

# current weather
from pyowm.owm import OWM
owm = OWM("a2ea2d41956d61479af803d9555ab68f")

# importing requests and json
import requests, json
# base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
CITY = "San Diego"
API_KEY = "a2ea2d41956d61479af803d9555ab68f"
# updating the URL
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
# HTTP request
response = requests.get(URL)
# checking the status code of the request
if response.status_code == 200:
   # getting data in the json format
   data = response.json()
   # getting the main dict block
   main = data['main']
   # getting temperature
   temperature = main['temp']
   # getting the humidity
   humidity = main['humidity']
   # weather report
   report = data['weather']
   a = f"Hey it's me, just a silly little worm in {CITY}."
   b = f"The current temperature in kelvin is: {temperature}."
   c = f"The Humidity level is: {humidity}."
   d = f"The cloud coverage looks like: {report[0]['description']}."
   my_list = [a, b, c, d]
else:
   # showing the error message
   print("Error in the HTTP request")

#schedule the tweet
import schedule
import time
def job():
#the code to get the tweet to print itself
   status = my_list[0] + " " + my_list[1] + " " + my_list[2] + " " + my_list[3]
   api.update_status(status)

schedule.every().day.at("18:50").do(job)
while 1:
   schedule.run_pending()
   time.sleep(1)




