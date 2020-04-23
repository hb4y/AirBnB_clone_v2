#!/usr/bin/python3
"""flask app"""

from flask import Flask, render_template
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


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python_string(text="is cool"):
    return 'Python ' + text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return str(n) + " is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def temp_number(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_odd(n):
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
