from flask import Flask, redirect, render_template, request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("base.html", title="/load_title?url=https://google.com")

@app.route("/load_title")
def load_title():
    try:
        url = request.args.get("url")
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        title = soup.title.string
        return render_template("index.html", title=title)
    except:
        return redirect("/load_title?url=https://google.com")
  
@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html', title='The requested URL was Not found')