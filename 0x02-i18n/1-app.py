#!/usr/bin/env python3
"""Contains the Flask application app """
from flask import Flask, render_template. request
from flask_babel import Babel


class Config(object):
    """Class that helps configure babel"""
    LANGUAGES = ['en', 'fr']


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """Render Home page """
    return render_template('1-index.html')


@babel.localeselector
def get_locale():
    """Get the locale for configuration """
    return app.config['BABEL_DEFAULT_LOCALE']


@babel.timezoneselector
def get_timezone():
    """Get the timezone for configuration """
    return app.config['BABEL_DEFAULT_TIMEZONE']


if __name__ == '__main__':
    app.run(debug=True)
