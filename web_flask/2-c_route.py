#!/usr/bin/python3
"""flask app"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<string:text>', strict_slashes=False)
def c(text):
    return 'C ' + text.replace("_", " ")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
