#!/usr/bin/python3
"""Starts Flask Web application That
Listening on 0.0.0.0:5000
Routes:
    / displays “Hello HBNB!”
    /hbnb displays “HBNB!”
    /c/<text> - display "C <text>" (replace underscore _ symbols with a space )
    /python/<text> - display "Python is cool"
    /number/<n> - display n if integer
Use the option strict_slashes=False in your route definition
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """prints Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """prints HBNB"""
    return "HBNB"


@app.route('/c/<string:text>', strict_slashes=False)
def c_text(text):
    """prints C followed by <text> content"""
    text = text.replace("_", " ")
    return "C %s" % text


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python_text(text="is cool"):
    """prints Python is cool"""
    text = text.replace("_", " ")
    return "Python %s" % text


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """display n if integer"""
    return "%i is a number" % n


if __name__ == "__main__":
    app.run(host="0.0.0.0")
