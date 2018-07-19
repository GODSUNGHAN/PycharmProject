import requests
from bs4 import BeautifulSoup
import os

for i in range (1,13): # 포 구문 선언 후 i 라는 임의의 문자를 넣어두자. 뭐 함수 f(x)같은 거네  그래서 범위는 1에서 12까지 (13바로 전까지 존재한다)
  month = str(i) #그리고 달(month)는 str 문자열로 바꾸어져야 한다.
  if i<10: # 그리고 i의 크기가 10보다 작을때는
    month = ( '0' + str(i))
  for j in range(1,30):
    day = str(j)
    if j < 10:
      day = ( '0' + str(j))


      requests = requests.get(url = "http://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId=105&date=2018"+str(month)+str(day))
      html = requests.text
      soup = BeautifulSoup(html, 'html.parser')
      list = soup.select('a.class=nclicks(rnk.sci)')

      my_titles = soup.select(
      'div.ranking_text > div.ranking_headline > a' #크롬에서 우클릭해서 카피>카피셀렉터
      )
    for title in my_titles:
      print(title.text)
      #print(title.get('href')) 태그 내부 내용만 가져온다.



