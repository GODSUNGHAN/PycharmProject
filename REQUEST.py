import requests
from bs4 import BeautifulSoup

reqSession = requests.session()
response = reqSession.get("http://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId=101&date=20180709/")
soup = BeautifulSoup(response.text,'html.parser')
soupResult = soup.findAll('li',{"class" :"ranking_item is_num1"})
soupResult = soup.findAll('li',{"class" :"ranking_item is_num2"})

print(str(soup))