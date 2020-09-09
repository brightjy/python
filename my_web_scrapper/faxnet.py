import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')
import requests
from bs4 import BeautifulSoup

URL = f'https://paxnetnews.com'
URL_ECONOMY = f'https://paxnetnews.com/categories/35?'

def get_last_page():
    result = requests.get(URL_ECONOMY)
    soup = BeautifulSoup(result.text, 'html.parser')
    pages = soup.find('div', {'class':'pagination'}).find_all('a')
    last_page = pages[-3].get_text(strip=True)
    return int(last_page)

def extract_article_detail(result):
    #title
    title = result.find('h1').find('a').text
    #sneakpeek
    sneakpeek = result.find("div",{"class":"desc"}).find('a').find('span').text
    #date
    date = result.find("div", {"class":"pubdate"}).text
    #key
    key = result.find('h1').find('a')['href']
    return {
        'title' : title,
        'sneakpeek' : sneakpeek,
        'date' : date,
        'link' : f'{URL}{key}'
    }

def extract_articles(last_page):
    articles = []
    for page in range(last_page):
        print(f"Scrapping page {page}")
        result = requests.get(f'{URL_ECONOMY}page={page}')
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all('div', {'class':'content'})
        for result in results:
            article = extract_article_detail(result)
            articles.append(article)
    return articles

def get_articles():
    last_page = get_last_page()
    articles = extract_articles(last_page)
    return articles