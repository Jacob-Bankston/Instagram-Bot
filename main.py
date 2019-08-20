# Importing the Instabot Library
from instabot import Bot

# Create our list to hold our hashtags
# remember to use snake_case
hashtag_list = ['100DaysOfCode', 'CodingLife', 'CodeNewbie', 'Python', 'JavaScript', 'Coding']

# Log into Instagram
bot = Bot()

bot.login()

#Create List to Hold Cities and Media IDs
cities_list = []
media_ids = []
constant = 1

# start logic here
# introduce while statement that runs until
# we pull back 1,000,000 cities in our list

while constant == 1:
  # Loop through our list of hashtags to search
  for hashtag in hashtag_list:
    for media in bot.get_hashtag_medias(hashtag):
      print(media)