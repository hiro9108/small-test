from flask import Flask,redirect,render_template,request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

soup = BeautifulSoup

@app.route("/")
def index():
    return render_template("index.html", title="Please add your query parameter to URL. Default is load_title?url=https://google.com")

@app.route("/load_title")
def load_title():
    try:
        url = request.args.get("url")

        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        result = soup.title.string

        print("--- Output ---")
        print("Title: ", result)
        print("--------------")

        return render_template("index.html", title=result)
    except:
        return redirect("/load_title?url=https://google.com")
  
@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html', title='The requested URL was Not found')