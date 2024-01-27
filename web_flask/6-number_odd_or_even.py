#!/usr/bin/python3
"""
Flask app
"""
from flask import Flask, abort, render_template


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


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
def snake(text='is cool'):
    """python route"""
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<n>", strict_slashes=False)
def integer_html(n):
    """number inspection"""
    try:
        if '.' not in n:
            n = int(n)
            return f"{n} is a number"
        else:
            raise TypeError
    except Exception:
        abort(404)


@app.route("/number_template/<n>", strict_slashes=False)
def number_template(n):
    """html rendering"""
    integer_html(n)
    n = int(n)
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<n>", strict_slashes=False)
def odd_or_even(n):
    """Tells if number is odd or even"""
    integer_html(n)
    n = int(n)
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
