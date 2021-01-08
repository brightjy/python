from flask import Flask, render_template, request, redirect
from scrapper import get_articles

app = Flask("SuperScrapper")

@app.route("/")
def home():
    return render_template("potato.html")

@app.route("/report")
def report():
    word = request.args.get('word')
    if word:
        # word가 있는 경우 대문자 입력처리
        word = word.lower() 
        articles = get_articles(word)
        print(articles)
    else:
        # word가 없는 경우 메인으로
        return redirect("/")
    return render_template("report.html", searchingBy=word)

app.run()