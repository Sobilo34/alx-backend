#!/usr/bin/env python3
"""A Flask app configured with Flask-Babel for i18n support."""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """A config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Find best language match
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    # Check locale from user settings
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')

    # Check locale from request header
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """
    The index function that render 0-app.py
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
