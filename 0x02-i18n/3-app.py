#!/usr/bin/env python3
"""Contains the Flask application app """
from flask import Flask, render_template, request
from flask_babel import Babel as Bab


class Config(object):
    """Class that helps configure babel"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    """Render Home page """
    return render_template('3-index.html')


# @babel.localeselector
def get_locale():
    """Get the locale for configuration"""
    return request.accept_languages.best_match(['fr'])
    # return request.accept_languages.best_match(app.config['LANGUAGES'])

babel = Bab(app, locale_selector=get_locale)
"""
@babel.timezoneselector
def get_timezone():Get the timezone for configuration
    return app.config['BABEL_DEFAULT_TIMEZONE']
"""

if __name__ == '__main__':
    app.run(debug=True)
