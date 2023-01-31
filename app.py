from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route("/")
def home():
    color = random.choice(["red", "yellow", "blue"])
    return render_template("home.html", color=color)


@app.route("/about")
def about():
    return render_template("about.html")
