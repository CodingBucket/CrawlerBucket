import requests
from bs4 import BeautifulSoup
from csv import writer


url = "http://jobs.bdjobs.com/jobsearch.asp?fcatId=8&icatId="

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

posts = soup.find_all(class_='job-title-text')

for post in posts:
    print(post.find('a').get_text().replace('\n',''))
    # title = post.find(class_='post-title').get_text().replace('\n', '')
    # link = post.find('a')['href']
    # date = post.select('.post-date')[0].get_text()