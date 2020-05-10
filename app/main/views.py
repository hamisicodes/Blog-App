from . import main
from flask import render_template
from flask_login import login_required

@main.route('/')
def index():
    title = 'welcome'
    return render_template('index.html', title=title)

@main.route('/blogs')
@login_required
def blogs():
    title = 'all blogs'
    return render_template('blogs.html', title=title)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

