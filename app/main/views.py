from . import main
from flask import render_template

@main.route('/')
def index():
    title = 'welcome'
    return render_template('index.html', title=title)

@main.route('/blogs')
def blogs():
    title = 'all blogs'
    return render_template('blogs.html', title=title)