from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/phyu")
def phyu():
    return "Welcome to my page"
