from flask import Flask, render_template, session, redirect, url_for
import random

app = Flask(__name__)

@app.route("/")
@app.route("/about")
def index():
    return render_template("about.html")

@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.debug = True
    app.run(host = "0.0.0.0", port = 8000)
