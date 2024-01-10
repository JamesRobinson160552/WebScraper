#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# File:          aholefinder.py                                                                   #
# Author:        James Robinson                                                                   #
# Purpose:       Alternative data gathering technique using selenium to increase collection rate #
# Last Modified: 01/10/2024                                                                       #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#Imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def AnalyzePost(postlink):
    driver.get(postlink)
    ps = driver.find_elements(By.TAG_NAME, 'p')
    for p in ps:
        print(p.text)

#Configure driver to run headless
options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)

#Main
AnalyzePost('https://www.reddit.com/r/AmItheAsshole/')

driver.quit()