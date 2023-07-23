#!/usr/bin/python3
"""Starts Flask Web application That
Listening on 0.0.0.0:5000
Routes:
    / displays “Hello HBNB!”
    /hbnb displays “HBNB!”
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


if __name__ == "__main__":
    app.run(host="0.0.0.0")
