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

#Configure driver to run headless
options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)

#Main
driver.get('https://reddit.com/r/AmItheAsshole')
print (driver.title)

driver.quit()