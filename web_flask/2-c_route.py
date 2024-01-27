#!/usr/bin/python3
"""
Flask app
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """
    app test
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """app test"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_fun(text):
    "c text"
    return f'C {text.replace("_", " ")}'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
