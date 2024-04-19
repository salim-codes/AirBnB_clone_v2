#!/usr/bin/python3
"""
    Start a Flask web application on 0.0.0.0, port 5000
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """Say hello to the client"""
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
