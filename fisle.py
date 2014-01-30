# -*- coding: utf-8 -*-
import sys
from flask import Flask, render_template
from flask.ext.flatpages import FlatPages, pygments_style_defs
from flask_frozen import Freezer
from flaskext.markdown import Markdown
from datetime import date, datetime

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)
Markdown(app)

def calculate_age(born):
    """Converts string to date object and calculates current age"""
    # Convert from string
    born = datetime.strptime(born, '%Y-%m-%d').date()
    today = date.today()
    try:
        birthday = born.replace(year=today.year)
    except ValueError: # leap year stuff
        birthday = born.replace(year=today.year, day=born.day-1)
    if birthday > today:
        return today.year - born.year - 1
    else:
        return today.year - born.year

@app.route('/')
@app.route('/index')
def index():
    """Index page. Lists articles if they have `date` field on them"""
    articles = (p for p in pages if 'date' in p.meta)
    # Newest first
    latest = sorted(pages, reverse=True,
            key=lambda p: p.meta['date'])
    return render_template('index.html', pages=latest)

@app.route('/archive')
def archive():
    """Lists titles of all entries"""
    articles = (p for p in pages if 'date' in p.meta)
    latest = sorted(pages, reverse=True,
            key=lambda p: p.meta['date'])
    return render_template('archive.html', pages=latest)

@app.route('/about')
def about():
    """About page"""
    birthday = '' # YYYY-MM-DD format
    age = calculate_age(birthday) # Calculates current age
    return render_template('about.html', age=age)

@app.route('/<path:path>/')
def page(path):
    """Fetches the correct .md file"""
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)


if __name__ == '__main__':
    """if run with build argument, generate the frozen pages
    else, run in debug mode"""
    if len(sys.argv) > 1 and sys.argv[1] == 'build':
        freezer.freeze()
    else:
        app.run(port=8000)
