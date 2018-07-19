import requests
from bs4 import BeautifulSoup
import os

requests = requests.get
    (url = "http://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId=105&date=201802020")
html = requests.text
soup = BeautifulSoup(html, 'html.parser')
list = soup.select('a.class=nclicks(rnk.sci)')

my_titles = soup.select(
    'div.ranking_text > div.ranking_headline > a')  # 크롬에서 우클릭해서 카피>카피셀렉터
for title in my_titles:
    print(title.text)
    # print(title.get('href')) 태그 내부 내용만 가져온다.

