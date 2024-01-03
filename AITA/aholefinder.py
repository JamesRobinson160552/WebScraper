#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# File:          aholefinder.py                                                                   #
# Author:        James Robinson                                                                   #
# Purpose:       Collect data from the subreddit r/AmItheAsshole to train a classifier.           #
# Last Modified: 11/29/2023                                                                       #
# TODO: Get more than 25 posts at a time? Deal with edge cases :(                                 #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#imports-------------------------------------------------------------------------------------------
from bs4 import BeautifulSoup #To parse HTML
import requests #To get HTML
from datetime import datetime #To get date for file naming
import traceback #To debug better
import time

filename = datetime.today().strftime('%Y-%m-%d') + '.json'
with open('./data/' + filename, 'w') as f:
    f.write("[")

#Ensures text pulled from posts is compatible with JSON
def clean_text(text):
    """Adds escape characters to double quotes.
    Removes leading and trailing whitespace."""
    clean_text = text.strip()
    clean_text = clean_text.replace('"', '\\"')
    return clean_text

#Analyze Post Function-----------------------------------------------------------------------------
def analyze_post(post_link):
    """Navigate to a specific post by link.
    Get the title, post body, and public decision.
    Store the above in a text file."""

    #Get post
    post = requests.get(post_link)
    postsoup = BeautifulSoup(post.text, 'lxml')

    #Parse for relevant data
    title = clean_text(postsoup.find('h1').text)
    paragraphs = postsoup.find_all('p')
    body = ""
    for paragraph in paragraphs[1:]:
        body += clean_text(paragraph.text)
    decision = clean_text(postsoup.find('shreddit-post-flair').text)

    #Store results in a JSON file
    print (title)
    print (body)
    print (decision)

    filename = datetime.today().strftime('%Y-%m-%d') + '.json'
    with open('./data/' + filename, 'a') as f:
        try:
            f.write("\n{\n\t\"title\" : \"" + title + "\",")
            f.write("\n\t\"body\" : \"" + body + "\",")
            if ('\U0001f4a9' in decision): #This handles decisions of 'Poo Mode' which include an unreadable character (poo emoji)
                decision = 'POO Mode'
            f.write("\n\t\"decision\" : \"" + decision + "\",")
            f.write("\n\t\"valid\" : \"true\" \n},")
        except: #This takes care of crash-causing edge cases, mostly unencodable chars atm
            f.write("\n\t\"valid\" : \"false\" \n},") #Since exceptions occur in the body typically, this maintains the JSON file format
            print("")
            traceback.print_exc()
            print("")

#Main----------------------------------------------------------------------------------------------
home = requests.get('https://www.reddit.com/svc/shreddit/community-more-posts/top/?t=WEEK&after=dDNfMTgyaGVnYg%3D%3D&name=AmItheAsshole&adDistance=3&feedLength=25')
homesoup = BeautifulSoup(home.text, 'lxml')
posts = homesoup.find_all('a', slot='full-post-link')

print (len(posts))
print (posts[0]['href'])\

for post in posts:
    analyze_post('https://www.reddit.com' + post['href'])

with open('./data/' + filename, 'a') as f:
    f.write("\n]\n")

f.close()
