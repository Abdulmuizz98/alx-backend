#!/usr/bin/env python3
"""Contains the Flask application app """
from flask import Flask, render_template
from flask_babel import Babel


class Config():
    """ """
    LANGUAGES = ['en', 'fr']
    TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """Render Home page """
    return render_template('0-index.html')


@babel.localeselector
def get_locale():
    return app.config['LANGUAGES'][0]


@babel.timezoneselector
def get_timezone():
    return app.config['TIMEZONE']


if __name__ == '__main__':
    app.run(debug=True)
