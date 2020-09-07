from thebell import extract_thebell_pages, extract_thebell_articles

last_thebell_page = extract_thebell_pages()

thebell_articles = extract_thebell_articles(last_thebell_page)

print(thebell_articles)