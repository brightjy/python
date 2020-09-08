import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')
import requests
from bs4 import BeautifulSoup

URL_MAIN = f"https://paxnetnews.com/categories/35?"
URL_ARTICLE = f"https://paxnetnews.com/articles/" 

def get_last_page():
    result = requests.get(URL_MAIN)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class":"pagination"})
    pages = pagination.find("span", {"class":"page"}).find_all("a")



def get_articles():
    last_page = get_last_page()
    return []