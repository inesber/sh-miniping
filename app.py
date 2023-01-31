from flask import Flask, render_template, request
import requests
import random
import time

app = Flask(__name__)


@app.route("/")
def home():
    color = random.choice(["red", "yellow", "blue"])

    panels = [
        {"title": "Goodreads", "url": "https://www.goodreads.com/"},
        {"title": "LinkedIn", "url": "https://www.linkedin.com/"},
        {"title": "Duolingo", "url": "https://www.duolingo.com/learn"},
        {"title": "Medium", "url": "https://medium.com/"},
        {"title": "It's Nice That", "url": "https://www.itsnicethat.com/"}
    ]

    return render_template("home.html", color=color, panels=panels)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/ping")
def ping():
    url = request.args.get("url")

    start_time = time.time()
    r = requests.get(url)
    end_time = time.time()

    diff_time = int((end_time - start_time) * 1000)

    return {
        "url": url,
        "code": r.status_code,
        "speed": diff_time
    }
