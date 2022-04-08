import main
from flask import Flask, render_template, flash

app = Flask(__name__)



@app.route("/")
def index():
    def myTestFunc(input):
        print(input)
        return input
    global myTest
    myTest = 'aiosduasoidausio'
    return render_template("index.html", myWord=myTest)
