import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')
import requests
from bs4 import BeautifulSoup

LIMIT = "10"
URL = "http://www.thebell.co.kr/free/content/Article.asp"

def extract_thebell_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    paging = soup.find("div", {"class":"paging"})
    pages = paging.find_all("a")
    thebell_pages = []
    for page in pages[1:-1]:
        thebell_pages.append(int(page.string))
    max_page = thebell_pages[-1]
    return max_page

def extract_thebell_articles(last_page):
    articles = []
    # for page in range(last_page):
    result = requests.get(f"{URL}?page={0*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser") 
    results = soup.find_all("dl")
    for result in results:
        title = result.find("a")["title"]
        date = result.find("span", {"class":"date"})
        print(title, date)
    return articles