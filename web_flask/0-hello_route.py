#!/usr/bin/python3
"""Starts Flask Web application That
Listening on 0.0.0.0:5000
Routes: / displays “Hello HBNB!”
Use the option strict_slashes=False in your route definition
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
