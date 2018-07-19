import urllib.request
from bs4 import BeautifulSoup
import time

url = "http://news.naver.com/main/ranking/popularDay.nhn?mid=etc&sid1=111"
response = urllib.request.urlopen(url)

soup = BeautifulSoup(response, "html.parser")
results = soup.select("#section_body. photo a")

for result in results
    print("제목 :", result.attrs ["title"])
    url_article = result.attrs ["herf"]
    response = urllib.request.urlopen(url_article)
    soup_article = BeautifulSoup(response, "html.parser")
    content = soup_article.select_one("#artivleBodyContents")

