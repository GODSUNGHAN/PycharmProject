import requests
from bs4 import BeautifulSoup
import re
import csv

session = requests.Session()
url = "http://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId=101&date=20180711"
response = session.get(url)
#print(response.text)
csvfile = open('news title.csv','w')


spamWriter = csv.writer(csvfile)

soup = BeautifulSoup(response.text, 'html.parser')

for i in range(30):
    soupResult = soup.findAll("li",{"class": "ranking_item is_num" + str(i+1)})
    exp = r"(?<=title=\").*(?=\"\s)"

    rex = re.search (exp, str(soupResult))

    if (rex is not None):
        print(rex.group(0))
        data = {"title" : str(rex.group(0))}
        json.dump(data, jsonfile)
        spamWriter.writerow([str(rex.group(0))])
        title = rex.group(0)

