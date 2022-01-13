from flask import Flask,render_template,request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

soup =BeautifulSoup

@app.route("/")
def index():
    return "Please add /load_title?url=https://google.com to your URL for example"

@app.route("/load_title")
def load_title():
    url = request.args.get("url")
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    result = soup.title.string

    print("--- Output ---")
    print("Title: ", result)
    print("--------------")

    return render_template("index.html", title=result)