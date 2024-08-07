#!/usr/bin/python3
'''This script starts Flask web app which 
runs on port 5000 by default
'''
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    return('Hello HBNB!')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
