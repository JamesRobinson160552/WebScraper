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
import time

filename = datetime.today().strftime('%Y-%m-%d') + '.json'
with open('./data/' + filename, 'w') as f:
    f.write("[")

#Analyze Post Function-----------------------------------------------------------------------------
def analyze_post(post_link):
    """Navigate to a specific post by link.
    Get the title, post body, and public decision.
    Store the above in a text file."""

    post = requests.get(post_link)
    postsoup = BeautifulSoup(post.text, 'lxml')

    title = postsoup.find('h1').text.strip()
    paragraphs = postsoup.find_all('p')
    body = ""
    for paragraph in paragraphs[1:]:
        body += paragraph.text.strip()
    decision = postsoup.find('shreddit-post-flair').text.strip()

    #Store results in a JSON file
    filename = datetime.today().strftime('%Y-%m-%d') + '.json'
    with open('./data/' + filename, 'a') as f:
        f.write("\n{\n\t\"title\" : \"" + title + "\",")
        f.write("\n\t\"body\" : \"" + body + "\",")
        f.write("\n\t\"decision\" : \"" + decision + "\"\n},")

    print (title)
    print (body)
    print (decision)

#Main----------------------------------------------------------------------------------------------
#test_post = 'https://www.reddit.com/r/AmItheAsshole/comments/17yohi6/aita_for_eating_at_the_children_i_babysit_fors/'
#analyze_post(test_post)

home = requests.get('https://www.reddit.com/svc/shreddit/community-more-posts/top/?t=WEEK&after=dDNfMTgyaGVnYg%3D%3D&name=AmItheAsshole&adDistance=3&feedLength=25')
homesoup = BeautifulSoup(home.text, 'lxml')
posts = homesoup.find_all('a', slot='full-post-link')

print (len(posts))
print (posts[0]['href'])
for post in posts:
    analyze_post('https://www.reddit.com' + post['href'])
f.write("\n]")


