import csv

def save_to_file(articles) :
    #open(or make) and save as 'file'
    file = open('articles.csv', mode='w', encoding='utf-8-sig')
    #write on the file
    writer = csv.writer(file)
    #write first row
    writer.writerow(['title', 'seakpeek', 'date', 'link'])
    #write articles
    for article in articles :
        #get dit{} values 
        writer.writerow(list(article.values()))
    return