#!/usr/bin/env python3
"""A Flask app configured with Flask-Babel for i18n support."""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """A congif class"""
    LANGUAUGE = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@app.route('/')
def index() -> str:
    """
    The index function that render 0-app.py
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
