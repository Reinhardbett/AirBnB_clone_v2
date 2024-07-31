#!/usr/bin/python3

"""
A script that starts a Flask web application:
and runs on port 5000
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return('HBNB')


@app.route('/c/<text>', strict_slashes=False)
def display_text(text):
    text = text.replace('_', ' ')
    return(f'C {text}')


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python_text(text="is cool"):
    text = text.replace('_', ' ')
    return(f'Python {text}')


@app.route('/number/<int:n>', strict_slashes=False)
def numbers(n):
    return(f'{n} is a number')


@app.route('/number_template/<int:n>', strict_slashes=False)
def n_temp(n):
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even(n):
    if n % 2 == 0:
        results = "even"
    else:
        results = "odd"
    return render_template("6-number_odd_or_even.html", n=n, results=results)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
