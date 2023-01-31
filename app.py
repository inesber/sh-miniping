from flask import Flask, render_template, request
import requests
import random

app = Flask(__name__)


@app.route("/")
def home():
    color = random.choice(["red", "yellow", "blue"])

    panels = [
        {"title": "Netflix", "url": "netflix.com"},
        {"title": "Youtube", "url": "youtube.com"},
        {"title": "Goodreads", "url": "goodreads.com"},
        {"title": "Duolingo", "url": "duolingo.com"}
    ]

    return render_template("home.html", color=color, panels=panels)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/ping")
def ping():
    url = request.args.get("url")

    return {
        "url": url,
        "code": "200",
        "speed": 400
    }
