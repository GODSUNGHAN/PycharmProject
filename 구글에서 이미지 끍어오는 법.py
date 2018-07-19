import requests
from bs4 import BeautifulSoup
import json


class crawler:
    def __init__(self):
        self.url = "https://www.google.com/search"
        self.keyword = "q="
        self.searchType = "tbm=isch"
        self.header = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
        self.session = requests.Session()


    def search(self,keyword_):
        targetUrl = self.url + "?"+self.keyword + keyword_ + "&" + self.searchType
        #print(targetUrl
        response = self.session.get(targetUrl, headers = {"User-agent" : self.header})
        #print(response.text)
        #print(response.text)
        soup = BeautifulSoup(response.text, "html.parser")
        sourpResult = soup.findAll("div",{"class":"rg_meta notranslate"})
        for i in range(10):
            link, type = json.loads(sourpResult[i].text)["ou"], json.loads(sourpResult[i].text)["ity"]
            print(link + ":" + type)
            fileinstance = open("filename"+str(i)+"."+type, 'wb')
            img_response = self.session.get(link)
            fileinstance.write(img_response.content)
            print("complete")


googleCrawler = crawler()
googleCrawler.search("apple")