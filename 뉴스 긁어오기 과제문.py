import requests
from bs4 import BeautifulSoup
import csv
import re

class NaverNewsCrawer
    def __init__(self):
        self.titleList = []
        self.session = requests.Session ()
        self.url = "http://news.naver.com/main/ranking/popularDay.nhn?mid=etc&sid1=111"


    def startCrawling(self):
        print("한달간의 뉴스 타이틀을 긁어옵니다.")
        response = self.session.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        for i in