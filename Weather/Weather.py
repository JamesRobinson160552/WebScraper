#imports-------------------------------------------------------------------------------------------
from bs4 import BeautifulSoup
import requests 
import time

html_text = requests.get("https://weather.gc.ca/city/pages/ns-17_metric_e.html").text
soup = BeautifulSoup(html_text, 'lxml')

content = soup.find('div', class_='div-table')
days = content.find_all('div', class_='div-column')
today = days[0]
print (today.text.strip())

for day in days[1:]:
    date = day.find('div', class_= 'div-row-head').text
    daytime = day.find('div', class_= 'div-row2')
    nighttime = day.find('div', class_= 'div-row4')

    daytime_temp = daytime.find('p', class_= 'high').text

    nighttime_temp = nighttime.find('p', class_= 'low').text


    print (daytime_temp)


#print (soup.prettify())