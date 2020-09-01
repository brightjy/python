#utf-8인코딩
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

#링크가져오기
import request딩

#beautifulSoup(웹크롤링 용이)
from bs4 import BeautifulSoup

thebell_result = requests.get("http://www.thebell.co.kr/free/content/Article.asp?svccode=00")

thebell_soup = BeautifulSoup(thebell_result.text, "html.parser")

paging = thebell_soup.find("div", {"class":"paging"})

pages = paging.find_all("a")

thebell_pages = []

for page in pages:
    thebell_pages.append(page.find)

print(thebell_pages[0:-1])