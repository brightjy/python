import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')
import requests
from bs4 import BeautifulSoup

LIMIT = "10"
URL_MAIN = "http://www.thebell.co.kr/free/content/Article.asp"
URL_ARTICLE = "http://www.thebell.co.kr/free/content/ArticleView.asp" 

def get_last_page():
    result = requests.get(URL_MAIN)
    soup = BeautifulSoup(result.text, "html.parser")
    paging = soup.find("div", {"class":"paging"})
    pages = paging.find_all("a")
    thebell_pages = []
    for page in pages[1:-1]:
        thebell_pages.append(int(page.string))
    max_page = thebell_pages[-1]
    return max_page

def extract_thebell_articles_from(html) :
    #scrapping title using select
    title_html = html.select('ul > li > dl > a > dt')
    for title in title_html:
        title = title.text
    #scrapping content using select
    content_html = html.select('ul > li > dl > a > dd')
    for content in content_html:
        content = content.text
    #scrapping date using class name
    date = html.find("span", {"class", "date"}).text
    #scrapping article key
    key_full = html.find("a")["href"]
    key_temp = key_full.strip('ArticleView.asp?key=')
    key = key_temp.strip('&lcode=00&page=1&svccode=00')
    return {
        'title': title, 
        'content': content, 
        'date': date, 
        "link": f"{URL_ARTICLE}?key={key}"
    }

def extract_articles(last_page):
    articles = []
    for page in range(last_page):
        print(f"Scrapping page {page}")
        result = requests.get(f"{URL_MAIN}?page={page*LIMIT}")
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all("div", {"class", "listBox"})
        for result in results:
            article = extract_thebell_articles_from(result)
            articles.append(article)
    return articles

def get_articles():
    last_page = get_last_page()
    articles = extract_articles(last_page)
    return articles