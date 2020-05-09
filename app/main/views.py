from . import main
from flask import render_template
from flask_login import login_required

@main.route('/')
def index():
    title = 'welcome'
    return render_template('index.html', title=title)

@main.route('/blogs')
def blogs():
    title = 'all blogs'
    return render_template('blogs.html', title=title)