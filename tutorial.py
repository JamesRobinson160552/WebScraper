#imports-------------------------------------------------------------------------------------------
from bs4 import BeautifulSoup
import requests 
import time

#Searches job posts on timesjobs.com, prints to console and saves each in a text file--------------
def search_jobs():
    #Get page - timesjobs.com with search term 'python' and make soup
    html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text
    soup = BeautifulSoup(html_text, 'lxml')

    #Find all job postings
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    #Loop through each job posting
    for index, job in enumerate (jobs):
        age = job.find('span', class_='sim-posted').span.text
        skills = job.find('span', class_='srp-skills').text.replace('  ,  ', ', ').strip()
        
        #If the job is recent and does not contain the excluded skill, print and save it
        if 'few' in age and skill_exclude not in skills:
            company_name = job.find('h3', class_='joblist-comp-name').text.strip()
            with open(f'job_posts/{company_name}.txt', 'w') as f:
                more_info = job.header.h2.a['href']

                f.write(f"Company Name: {company_name}\n")
                f.write(f"Required Skills: {skills}\n")
                f.write(f"More Info: {more_info} \n")

                print(f'Saved as: {company_name}.txt')
                print(f"Company Name: {company_name}")
                print(f"Required Skills: {skills}")
                print(f"More Info: {more_info} \n")

#Main----------------------------------------------------------------------------------------------
waitTime = 600 #Find jobs every x seconds
skill_exclude = input('Exclude skill: ') #Ecludes postings with this keyword
while True:
    search_jobs()
    time.sleep(waitTime)

