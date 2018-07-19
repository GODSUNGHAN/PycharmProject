import requests
from bs4 import BeautifulSoup
import os



for i in range (1,13):
  month = str(i)
  if i<10:
    month = ( '0' + str(i))
  for j in range(1,30):
    day = str(j)
    if j < 10:
      day = ( '0' + str(j))
    print ("2018"+month+day)
    requests = requests.get(url = "http://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId=105&date="+i(1)+j(1))
    html = requests.text
    soup = BeautifulSoup(html, 'html.parser')
    list = soup.select('a.class=nclicks(rnk.sci)')

    my_titles = soup.select(
        'div.ranking_text > div.ranking_headline > a'
    )

    for title in my_titles:
        print(title.text)





