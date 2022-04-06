from flask import Flask, render_template, flash

app = Flask(__name__)

myTest = "Epic"

@app.route("/")
def index():
    return render_template("index.html")
