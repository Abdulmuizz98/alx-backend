#!/usr/bin/env python3
"""Contains the Flask application app """
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


@app.route('/')
def index():
    """Render Home page """
    return render_template('0-index.html')
# babel = Babel(app)


if __name__ == '__main__':
    app.run(debug=True)
